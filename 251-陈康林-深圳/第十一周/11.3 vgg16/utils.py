import matplotlib.image as mpimg
import tensorflow as tf
import numpy as np

def load_image(path):
    #读取图片
    img = mpimg.imread(path)
    #将图片转成正方形
    short_edge = min(img.shape[:2])
    yy = int((img.shape[0] - short_edge) / 2)
    xx = int((img.shape[1] - short_edge) / 2)
    corp_img = img[yy:short_edge + yy,xx:short_edge + xx]
    return corp_img
def resize_image(image,size,method=tf.image.ResizeMethod.BILINEAR,align_corners = False):
    with tf.name_scope('resize_image'):
        image = tf.expand_dims(image,0)
        image = tf.image.resize_images(image,size,method,align_corners)
        image = tf.reshape(image,tf.stack([-1,size[0],size[1],3]))
        return image
def print_prob(prob,file_path):
    synset = [l.strip() for l in open(file_path).readlines()]
    # 将概率从大到小排列的结果的序号存入pred
    preb = np.argsort(prob)[::-1]
    top1 = synset[preb[0]]
    print('top1',top1,prob[preb[0]])
    top5 = [(synset[preb[i]],prob[preb[i]]) for i in range(5)]
    print('top1',top5)
    return top1