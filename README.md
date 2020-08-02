# Mask-recognition-and-detection-based-on-ZCU104
Mask recognition and detection based on ZCU104


# 2020年新工科联盟-Xilinx暑期学校（Summer School）项目

# 1.网络裁剪
  
# 2.Vitis-AI的使用
## 2.0 Vitis-AI的下载
  如果已经安装了Vitis-AI请跳过本步骤。
  如没有安装Vitis—AI,在Ubuntu下完成Vitis—AI的下载请参考Xilinx官网链接https://github.com/Xilinx/Vitis-AI 。  
## 2.1 量化/AI Quantizer
  #### 量化对象为/mask3/mask.pb
  Vitis-AI的量化过程是将权重和偏置由float32转成int8。
  在量化过程中需要参考input_fn.py和image_path.py完成量化时图片的读取。量化时，图片数量原则上不少于50个，无需带有标签。
  先执行image_path.py会生成一个train.txt文件，然后在input_fn.py中指定该.txt文件即可。
  
  接着在执行如下量化命令：（PS:--calib_iter参数 = 量化总图片数 / batch_size）
  
  vai_q_tensorflow quantize --input_frozen_graph face_mask_detection.pb --input_nodes data_1 --input_shapes ?,260,260,3 --output_nodes cls_4_conv_1/BiasAdd,loc_4_conv_1/BiasAdd,loc_3_conv_1/BiasAdd,cls_3_conv_1/BiasAdd,cls_2_conv_1/BiasAdd,loc_2_conv_1/BiasAdd,cls_1_conv_1/BiasAdd,loc_1_conv_1/BiasAdd,cls_0_conv_1/BiasAdd,loc_0_conv_1/BiasAdd  --input_fn input_fn.calib_input --method 1 --gpu 0 --calib_iter 1000 --output_dir ./quantize_results 

  量化评估可以参考官方文档完成，此部分不再详细描述。
## 2.2 编译
  在Vitis—AI中执行一下命令完成编译：
  
vai_c_tensorflow  --frozen_pb /workspace/quan_results/deploy_model.pb  --arch /opt/vitis_ai/compiler/arch/dpuv2/ZCU104/ZCU104.json  --output_dir ./comp_results  --net_name mask --options "{'mode':'normal'}"
 
 通过上述命令会在comp_results文件夹下产生dpu_mask.elf文件。（该文件已经放在model下可以直接使用）

# 3.ZCU104的配置和使用
 下载对应的官方镜像并完成必须的配置。
  通过SSH将整个mask3传输到ZCU104板卡中（PS如果显示图片启动ssh时需要配置X11）。
  进入到mask3文件中，输入 python mask3.py model/ 即可运行并得到识别后的图片和结果。此例子结果为91%。
# 4.结果
  ![image](https://github.com/CCXDB/Mask-recognition-and-detection-based-on-ZCU104/tree/master/result/result.png)
