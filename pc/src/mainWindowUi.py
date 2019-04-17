#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
ISOTIMEFORMAT = '%Y_%m_%d_%H_%M_%S'

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindowUi(QMainWindow, QWidget):
    """主窗口Ui"""
    def __init__(self):
        super().__init__()  
        self.setupMainWindow()   

    def setupMainWindow(self):
        """初始化主窗口"""
        self.setupUi()
        self.setupLayout()
        
    def setupUi(self):
        """初始化主窗口Ui"""
        self.createButton()
        self.createImageLabel()
        self.createSaveFrameLabel()

    def showUi(self):
        """显示主窗口"""
        self.show()
        self.setWindowIcon(QIcon("./icon/rpi.png"))
        
    def createButton(self):
        """创建按钮"""
        self.openLocalCameraButton = QPushButton("打开本地摄像头", self)
        self.closeLocalCameraButton = QPushButton("关闭本地摄像头", self)
        
        self.openVideoButton = QPushButton("打开视频", self)
        self.closeVideoButton = QPushButton("关闭视频", self)
        self.openAFrameImageButton = QPushButton("打开图片", self)
        
        self.webCameraIPLabel = QLabel("IP地址",self)
        self.webCameraIPLineEdit = QLineEdit(self)
        self.webCameraIPLineEdit.setText("169.254.196.152")
        self.webCameraPortLabel = QLabel("端口",self)
        self.webCameraPortLineEdit = QLineEdit(self)
        self.webCameraPortLineEdit.setText("22")
        self.pingIPButton = QPushButton("检测IP地址", self)
        self.openWebCameraButton = QPushButton("打开网络摄像头", self)
        self.closeWebCameraButton = QPushButton("关闭网络摄像头", self)

     
    def createImageLabel(self):
        """创建图像标签"""
        # 图像的标签
        self.imageToShow = QImage()
        self.imageToShowLabel = QLabel(self)
        if self.imageToShow.load("./icon/blank_640x480.jpg"):
            self.imageToShowLabel.setPixmap(QPixmap.fromImage(self.imageToShow))
        # 检测结果图像的标签
        self.resultImage = QImage()
        self.resultImageLabel = QLabel(self)
        if self.resultImage.load("./icon/blank_256x128.jpg"):
            self.resultImageLabel.setPixmap(QPixmap.fromImage(self.resultImage))

    def createSaveFrameLabel(self):
        """创建保存图像标签"""    
        
        self.savePathLabel = QLabel("保存路径",self)
        self.savePathLineEdit = QLineEdit(self)
        self.savePathLineEdit.setText("C:/rpi_save/cam1")
        
        self.autoSaveButton = QRadioButton('视频帧自动保存', self) 
        
       
    def setupLayout(self):
        """初始化布局"""
        self.createGroupBox_For_AFrameImage()
        self.createGroupBox_For_Video()
        self.createGroupBox_For_LocalCamera()
        self.createGroupBox_For_ImageToShow()
        self.createGroupBox_For_SaveFrame()
        self.createGroupBox_For_WebCamera()

        leftSideLayout = QVBoxLayout() 
        leftSideLayout.addWidget(self.aFrameImageGroupBox)
        leftSideLayout.addWidget(self.videoGroupBox)
        leftSideLayout.addWidget(self.localCameraGroupBox)
        leftSideLayout.addWidget(self.webCameraGroupBox)
        leftSideLayout.addStretch()# 在最后一个控件之后添加伸缩，这样所有的控件就会居上显示
         
        rightSideLayout = QVBoxLayout()
        rightSideLayout.addWidget(self.saveFrameGroupBox)
        rightSideLayout.addStretch() 
         
         
        mainLayout = QHBoxLayout() 
        mainLayout.addLayout(leftSideLayout)
        mainLayout.addWidget(self.imageToShowGroupBox)
        mainLayout.addLayout(rightSideLayout)
        mainLayout.addStretch()# 在最后一个控件之后添加伸缩，这样所有的控件就会居左显示
        
        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)    
        
    def createGroupBox_For_AFrameImage(self):
        """单张图片的GroupBox"""
        self.aFrameImageGroupBox = QGroupBox("aFrameImage")
        layout = QVBoxLayout()
        layout.setSpacing(10) 
        layout.addWidget(self.openAFrameImageButton)
        self.aFrameImageGroupBox.setLayout(layout)
        
    def createGroupBox_For_Video(self):
        """视频的GroupBox"""
        self.videoGroupBox = QGroupBox("video")
        layout = QVBoxLayout()
        layout.setSpacing(10) 
        layout.addWidget(self.openVideoButton)
        layout.addWidget(self.closeVideoButton)
        self.videoGroupBox.setLayout(layout)      
        
        
    def createGroupBox_For_LocalCamera(self):
        """本地摄像头的GroupBox"""
        self.localCameraGroupBox = QGroupBox("localCamera")
        layout = QVBoxLayout()
        layout.setSpacing(10) 
        layout.addWidget(self.openLocalCameraButton)
        layout.addWidget(self.closeLocalCameraButton)
        self.localCameraGroupBox.setLayout(layout)  
        
    def createGroupBox_For_WebCamera(self):
        """网络摄像头的GroupBox"""
        self.webCameraGroupBox = QGroupBox("webCamera")
        layout = QVBoxLayout()
        layout.setSpacing(10)      
        layout.addWidget(self.webCameraIPLabel)
        layout.addWidget(self.webCameraIPLineEdit)
        layout.addWidget(self.webCameraPortLabel)
        layout.addWidget(self.webCameraPortLineEdit)
        layout.addWidget(self.pingIPButton)
        layout.addWidget(self.openWebCameraButton)
        layout.addWidget(self.closeWebCameraButton)
        self.webCameraGroupBox.setLayout(layout)  
        

    def createGroupBox_For_ImageToShow(self):
        """图像的GroupBox"""
        self.imageToShowGroupBox = QGroupBox("imageToShow")
        layout = QVBoxLayout()
        layout.setSpacing(10) 
        layout.addWidget(self.imageToShowLabel)
        self.imageToShowGroupBox.setLayout(layout)  
        
    def createGroupBox_For_SaveFrame(self):
        """保存视频帧的GroupBox"""
        self.saveFrameGroupBox = QGroupBox("saveFrame")
        layout = QVBoxLayout()
        layout.setSpacing(10) 
        layout.addWidget(self.savePathLabel)
        layout.addWidget(self.savePathLineEdit)
        layout.addWidget(self.autoSaveButton)
        self.saveFrameGroupBox.setLayout(layout)     
          




        
        