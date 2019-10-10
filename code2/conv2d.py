#coding=utf-8

import numpy as np 
import cv2 


class Conv2d(object):
    def __init__(self, features, size, stride=1, padding="Same", bias=False):
        super(Conv2d, self).__init__()
        self.features = features
        self.ch_in, self.k_w, self.k_h, self.ch_out = size
        self.stride = stride 
        self.padding = padding 
        self.bias = bias 
        # self.kernel = np.random.rand(self.ch_in, self.k_w, self.k_h, self.ch_out)
        self.kernel = np.zeros(size)
        for i in range(self.k_w):
            self.kernel[i, 0, i, i] = 1.0
        _, self.w_in, self.h_in, _ = features.shape
        self.w_out = self.w_in // self.stride 
        self.h_out = self.h_in // self.stride 
        self.feature_out = None
        self.forward()
    
    def featurePadding(self):
        b, w, h, d = self.features.shape
        try:
            assert self.ch_in == d  
            if self.padding == "Invalid":
                features_pad = self.features 
            else:
                pad_l = self.k_w // 2 
                pad_r = self.k_w - pad_l - 1
                pad_u = self.k_h // 2
                pad_d = self.k_h - pad_u - 1
                padding_size = ((0, 0), (pad_l, pad_r), (pad_u, pad_d), (0, 0))
                if self.padding == "Same":
                    padding_mode = "constant"
                elif self.padding == "Reflect":
                    padding_mode = "reflect"
                elif self.padding == "Symmetric":
                    padding_mode = "symmetric"
                features_pad = np.pad(self.features, padding_size, padding_mode)
        except AssertionError:
            print("Kernel size must match the depth of input features!")
        return features_pad 
    
    def conv2d(self, features_in):
        b, w, h, d = features_in.shape
        features_out = []
        kernel = self.kernel.reshape(-1, self.ch_out)
        for k in range(b):
            features_flatten = []
            for i in range(0, h - self.k_w + 1, self.stride):
                for j in range(0, w - self.k_h + 1, self.stride):
                    patch = features_in[k, i:i+self.k_w, j:j+self.k_h, :]
                    patch_flattern = patch.reshape(-1)
                    features_flatten.append(patch_flattern)
            features_flatten = np.stack(features_flatten, axis=0)
            features_out_t = np.matmul(features_flatten, kernel)
            features_out_t = np.resize(features_out_t, (self.w_out, self.h_out, self.ch_out))
            features_out.append(features_out_t)
        features_out = np.stack(features_out, axis=0)
        return features_out
    
    def forward(self):
        feature_pad = self.featurePadding()
        self.feature_out = self.conv2d(feature_pad)
        
    def backward(self):
        pass 


def conv2dLayer(data_in, ksize, stride=1, padding="Same", bias=False):
    data_out = Conv2d(data_in, (3, 3, 3, 3), stride)
    return data_out.feature_out


if __name__ == "__main__":
    img = cv2.imread("./../data/00.jpg")
    img = cv2.resize(img, (512, 512))
    data_in = np.expand_dims(img, 0)
    feature_o = conv2dLayer(data_in, (3, 5, 5, 3), 2) 
    feature_o = np.array(feature_o, dtype=np.uint8)
    print(feature_o.shape)
    cv2.imshow("img", feature_o[0])
    cv2.waitKey()


