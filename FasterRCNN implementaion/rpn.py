import torch
import torch.nn as nn
import torchvision
import math

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class RegionPraposalNetwork(nn.Module):
    def __init__(self,in_channels = 512):
        self.scales = [ 128,256,512]
        self.aspect_ratios = [0.5,1,2]
        self.num_anchors = len(self.scales)*len(self.aspect_ratios)

        #3x3 conv layer
        self.rpn_conv = nn.Conv2d(in_channels,in_channels,kernel_size=3,stride=1,padding=1)         
        
        #1x1 classification layer
        self.cls_layer = nn.Conv2d(in_channels,self.num_anchors,kernel_size=1,stride=1)
        
        #1x1 regression layer
        self.bbox_reg_layer = nn.Conv2d(in_channels,self.num_anchors*4,kernel_size=1,stride=1)

    def generate_achors(self,image,feat):

        grid_h,grid_w = image.shape[:2]
        image_h,image_w = image.shape[:2]

        strid_h = torch.tensor(image_h//grid_h,
                                dtype=torch.int64,
                                device=feat.device)
        strid_w = torch.tensor(image_w//grid_w,
                                dtype=torch.int64,
                                device=feat.device)
         
        scales = torch.as_tensor(self.scales,
                                 dtype=feat.dtype,
                                 device=feat.device)
        aspect_ratios = torch.as_tensor(self.aspect_ratios,
                                        dtype=feat.dtype,
                                        device=feat.device)

    def forward(self, image,feat,target):

        #call rpn layer
        rpn_feat = nn.ReLU()(self.rpn_conv(feat))
        cls_scores = self.cls_layer(rpn_feat)
        box_transform_pred = self.bbox_reg_layer(rpn_feat)

        #generate achors
        anchors = self.generate_achors(image,feat)
