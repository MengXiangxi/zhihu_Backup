# zhihu_Backup
知乎个人回答备份，获取html并打印到pdf

## 缘起和功能
[知乎](https://www.zhihu.com)是中文互联网中流量很高的社会化问答网站。我自2011年起一直是知乎的用户，见证了该平台的兴衰。然而近来，知乎管理人员出于不明原因，粗暴侵犯部分用户的基本权利，侵害了我使用其服务的基础，使我无法在该平台上发表内容。有鉴于此，我决定备份本用户既往在知乎上发表的全部回答，并随后删除之。

知乎没有提供官方的接口，但程序员[七秒不觉梦](https://github.com/7sDream/)提供了他尝试解析出的OAuth2接口。这一项目具有非常高的质量，也是本工作的最重要的基础。在此对开发者表示敬意。由于html外链一些图片文件仍可能依赖知乎的服务器数据，故在下载后将其打印到pdf文件，保持独立性。

本工作包括三个简单的脚本。它们的功能是在根目录下备份当前用户全部回答。在这一框架基础上稍加改写，也可以用于和知乎相关的其它数据获取任务。

## 依赖关系和运行环境
- Python 3.6
- [Zhihu-Oauth](https://github.com/7sDream/zhihu-oauth)（python库：zhihu_oauth）
- [Python-PDFKit](https://github.com/JazzCore/python-pdfkit)（python库：pdfkit），该库依赖于[wkhtmltopdf](https://wkhtmltopdf.org/)

本脚本在Windows 10下测试通过，但理论上在Linux和macOS上也是可用的。

## 脚本执行顺序和功能
顺序 | 文件名 | 功能
---- | --- | ---
1 | zhihu_login.py | 登录知乎并保存token
2 | zhihu_backup.py | 获取个人动态中全部回答的信息，并创建html文件
3 | zhihu_html2pdf.py | 将获取的html文件保存成PDF
— | 各html和pdf文件 | 输出样例

测试数据来自[本知乎账户](https://www.zhihu.com/people/mengxiangxi)，测试完成后已经手动删除全部历史回答，但可见仍有大量信息保存在知乎服务器上或无法删除。

## 已知问题
- PDF不支持部分多媒体文件的备份，如动图等。
- 我觉得评论内容不重要，就没有予以备份。如有需求可自行修改。
