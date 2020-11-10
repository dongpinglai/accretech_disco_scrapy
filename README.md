## README
* ### 项目说明：
> 基于python, scrapy框架的爬虫，爬取accretech和DISCO的产品信息。各项产品信息将生成pdf文件
* ### 使用说明：
> 略
* ### 注意事项：
1. pdfkit 需要下载安装依赖wkhtmltopdf(https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf)，下载地址如下:
https://wkhtmltopdf.org/downloads.html

2. 中文字体乱码：

>原因：服务器中没有安装中文字体包，所以wkhtmltopdf中的webkit无法识别中文

>解决方案：
>>1.Windows字体目录为C:\Windows\Fonts\，将需要的字体文件拷贝到Linux中/usr/share/font并解压(可以预先在此目录新建chinese文件夹

>>2.$ fc-cache -fv