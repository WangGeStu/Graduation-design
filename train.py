import sys
import torch
import torchvision 
from cnn_finetune import make_model
from sklearn import metrics
#from utils import *
class ImageClassfication:

    #parameter
    batch_size=20
    epoch=100
    lr=0.003
    momentum=0.9#加速收敛
    weight_decay=5e-4#权值衰减  防止过拟合
    
    def __init__(self,device=None):
        #device
        if not device:
            self.device=torch.device( "cuda" if torch.cuda.is_available()else "cpu")
            print("default device:",self.device)
        else:
           
            self.device=torch.device(device)
            print("device:",self.device)
            
    def load_dataset(self,dataroot):
        """load dataset return dataloder"""

        #transforms
        transform=torchvision.transforms.Compose([
                torchvision.transforms.RandomResizedCrop((224,224)),#任意裁切
                torchvision.transforms.RandomHorizontalFlip(),#0.5概率随机水平翻转
                torchvision.transforms.RandomVerticalFlip(),  # 以0.5的概率垂直翻转
                torchvision.transforms.RandomRotation(10),  # 在（-10， 10）范围内旋转
                torchvision.transforms.ColorJitter(0.05, 0.05, 0.05, 0.05),  # HSV以及对比度变化
                torchvision.transforms.ToTensor(),
                torchvision.transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))

                ])
        #dataset
        self.dataset=torchvision.datasets.ImageFolder(root=dataroot,transform=transform)
        #the number of classes
        self.num_classes=len(self.dataset.classes)
        #the number of data
        self.dataset_size=len(self.dataset)
        #the number of each class
        self.eachclass_size=[0]*self.num_classes
        for i in self.dataset.targets:
            self.eachclass_size[i]+=1     
            
        print("dataset's len =",len(self.dataset))    
        print("eachclass_size =",self.eachclass_size)
        #dataloader
        self.dataloader=torch.utils.data.DataLoader(self.dataset,batch_size=self.batch_size,shuffle=True,pin_memory=True,num_workers=0)
 
      
        return self.dataloader
    def load_val_dataset(self,dataroot):
        """load val dataset return dataloder"""
        #transforms
        transform=torchvision.transforms.Compose([
                torchvision.transforms.Resize(256),#缩放
                torchvision.transforms.CenterCrop(224),#中心裁切
                torchvision.transforms.ToTensor(),
                torchvision.transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))                
                ])
        self.val_dataset=torchvision.datasets.ImageFolder(root=dataroot,transform=transform)
        self.val_dataloader=torch.utils.data.DataLoader(self.val_dataset,batch_size=self.batch_size,shuffle=False,pin_memory=True,num_workers=0)
 
      
        return self.val_dataloader

    def load_model(self,modelname,pretrained=True):
        """load model return model"""
        model=make_model(modelname, num_classes=self.num_classes, pretrained=pretrained)

        
        model=model.to(self.device)        
 
        if "cuda" in str(self.device) :
            model=torch.nn.DataParallel(model)
        self.model=model
        self.modelname=modelname
        print(modelname)
        return model
         
    def save_model(self,model,path):
        """save model"""
        torch.save(model,path)
        model=model.to(self.device)

    def train_model(self):
        """train model"""

        #set optim
        self.opt=torch.optim.SGD(self.model.parameters(),lr=self.lr,momentum=self.momentum, weight_decay=self.weight_decay)
        
        #<<< get classes_weight============================
        mulsum=1
        classes_weight=[0]*self.num_classes
        for i in self.eachclass_size:
            mulsum*=i
        for i in range(self.num_classes):
            classes_weight[i]= mulsum/ self.eachclass_size[i] 
        classes_weight=torch.tensor(classes_weight,device=self.device)
        classes_weight=classes_weight/torch.sum(classes_weight)
        print("classweight:",list(classes_weight.cpu().numpy()))   #损失比例
        #>>> get classes_weight finish======================
        
        #set lossfunction
        self.lossfunction=torch.nn.CrossEntropyLoss( classes_weight )
        #self.lossfunction=focal_loss(num_classes=self.num_classes)
        
        self.accmax=-100
        # each epoch==================================================================
        for i in range(self.epoch):
            losssum=0.0
            labellist=[]
            resultlist=[]
            print("========================================\nepoch",i,":")
            #train=======================================================
            #set model mode  
            self.model.train() #启用BatchNormalization和Dropout
            
            #each train batch============================== 
            for input,label in self.dataloader:
                
                #record label 
                labellist.extend(label.numpy())
                
                #send tensor to device
                input=input.to(self.device)
                label=label.to(self.device)
                #empty grad
                self.opt.zero_grad() 
                #forward and get loss
                result=self.model(input)                
                loss=self.lossfunction(result,label)
                #get grad for each weight
                loss.backward()
                
                result = result.argmax(dim=1)
                losssum+=loss.item()*input.size(0)
                #record result
                resultlist.extend(result.cpu().numpy())
                
                
                self.opt.step()
            #each train batch finish======================== 
            
            
            #print each epoch result
            print("train:")
            print("loss:",losssum/self.dataset_size)
            #classification_report 函数用于显示主要分类指标的文本报告，在报告中显示每个类的精确度、召回率、F1值等信息
            #F1—Score，用来衡量二分类模型精确度的一种指标。它同时兼顾了分类模型的精确率和召回率。可以看作是模型精确率和召回率的一种调和平均，它的最大值是1，最小值是0。
            #y_true = labellist:1维数组，或标签指示器数组/稀疏矩阵，目标值
            #y_pred = resultlist:1维数组,或标签指示器数组/稀疏矩阵，分类器返回的估计值 (也就是result)
            #target_names:字符串列表，与标签匹配的可选显示名称（顺序相同）
            #digits:int,输出浮点值的位数
            print(metrics.classification_report(labellist,resultlist,target_names=[str(i) for i in range(self.num_classes)],digits=4))

            #val===========================================================            
            resultlist=[]
            labellist=[]
            #set model mode   
            self.model.eval()  #不启用BatchNormalization和Dropout
            #each val batch========================= 
            for input,label in self.val_dataloader:
                #record label 
                labellist.extend(label.numpy())
                #send tensor to device
                input=input.to(self.device)
                label=label.to(self.device)
                
                result=self.model(input) 
                result = result.argmax(dim=1)
                #record result
                resultlist.extend(result.cpu().numpy())
            #each val batch finish==================
            print("val:")
            print(metrics.classification_report(labellist,resultlist,target_names=[str(i) for i in range(self.num_classes)],digits=4))

            #save model
            result_dict=metrics.classification_report(labellist,resultlist,target_names=[i for i in range(self.num_classes)],digits=4,output_dict=True)
            if self.accmax < result_dict['macro avg']["f1-score"]:
                self.accmax= result_dict['macro avg']["f1-score"] 
                self.save_model(self.model,self.modelname+"_"+str(i)+".pth")

            
        #each epoch finish==============================================================

def get_finished_model(modelname,dataroot):
    m=ImageClassfication()
    m.load_dataset(dataroot=dataroot+"/train/")
    m.load_val_dataset(dataroot=dataroot+"/val/")
    m.load_model(modelname)
    m.train_model()
    return m.model
    
if __name__=="__main__":
    dataroot=r".\data"
    modelname='resnet50'
    model=get_finished_model(modelname=modelname,dataroot=dataroot)
    
