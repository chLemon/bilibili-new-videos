# bilibili-new-videos

自己对关注的 UP 进行分类，分类展示他们最近的更新

## 背景

最近关注了很多新的 up，导致关注列表填入了大量视频。休息的时候只想看一些轻松的视频，但是 B 站动态列表不能进行分类。

核心诉求：

1. 爬取指定 up 主的视频动态
2. 存储 up 分类信息
3. 记录已经看过的部分

## 实现和使用

在 bilibili-new-videos/data/我的 up 分组.md 中填写自己关注的 UP 信息。

然后运行 bilibili-new-videos/bilibili-new-videos-dev.ipynb

会将近期的更新写在 bilibili-new-videos/output/ 下

## 爬取实现

使用 https://github.com/SocialSisterYi/bilibili-API-collect?tab=readme-ov-file 提供的 API
