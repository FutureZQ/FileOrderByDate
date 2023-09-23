# FileOrderByDate

## 编写原因 Reason to writing
在onedrive某次更新中，onedrive启用了将照片按照月份和日期的文件夹存放的功能，但是功能打开前的照片却摆在外面，显得很乱。所以写一个脚本将onedrive图片按月份和日期归类。

In an update of OneDrive, OneDrive enabled the ability to store photos in folders by month and day, but the photos before the feature was turned on were placed outside, which looked messy. So write a script to categorize OneDrive images by month and day.

## 使用方法 How to use
```
python move_file_by_date.py
```

## 已知问题 Known issues

如果文件位于云盘中，可能会将文件下载到本地

If the file is located in a cloud disk, the file may be downloaded locally