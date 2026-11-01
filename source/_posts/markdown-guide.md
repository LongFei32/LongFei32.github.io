---
title: 写作模板：Markdown 速查
date: 2026-11-01 23:10:00
categories:
  - 学习笔记
tags:
  - Markdown
  - 工具
---

这篇不是给人看的，是给我自己看的——以后忘了 Markdown 怎么写，就打开这一篇抄。

<!-- more -->

新建文章的命令：

```bash
hexo new "文章标题"
```

会在 `source/_posts/` 下生成一个 `.md` 文件，打开就能写。

## 标题

```markdown
# 一级标题（一般不用，文章标题已经有了）
## 二级标题
### 三级标题
```

## 强调

```markdown
**加粗**
*斜体*
~~删除线~~
`行内代码`
```

效果：**加粗**、*斜体*、~~删除线~~、`行内代码`。

## 列表

```markdown
- 无序项
- 另一项
  - 嵌套

1. 有序项
2. 第二项
```

## 引用

```markdown
> 这是一段引用。
> 可以写多行。
```

## 代码块

三个反引号包起来，后面跟语言名就能高亮：

````markdown
```python
import numpy as np
x = np.arange(10)
```
````

## 表格

```markdown
| 方法 | 优点 | 缺点 |
| --- | --- | --- |
| 静态站 | 免费、快 | 没有后端 |
| 动态站 | 功能全 | 要服务器 |
```

## 链接与图片

```markdown
[链接文字](https://example.com)

![图片说明](/img/avatar.png)
```

图片放在 `source/img/` 下，引用时写 `/img/文件名`。

## 摘要分隔

在正文里插入这一行，它上面的内容会作为首页摘要：

```markdown
<!-- more -->
```

## 文章头部（Front-matter）

每篇文章开头那段 `---` 包起来的部分：

```yaml
---
title: 文章标题
date: 2026-11-01 23:10:00
categories:
  - 学习笔记
tags:
  - Markdown
---
```

`categories` 只能有一个层级，`tags` 可以随便加。分类和标签页会自动生成，不用手动维护。

---

先记这些，够用了。真忘了就去查 [Markdown 官方教程](https://www.markdownguide.org/)。
