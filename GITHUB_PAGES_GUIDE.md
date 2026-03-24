# GitHub Pages 启用指南

## 📖 概述
本指南将帮助您启用GitHub Pages，使预览页面可以通过网页直接访问。

## 🔗 当前状态
- ✅ 预览文件已上传到GitHub仓库
- ⚙️ GitHub Pages待启用
- 🌐 访问地址: https://yimuyiguo.github.io/open-curtain-calc/

## 🚀 启用步骤

### 方法一：通过GitHub网页界面（推荐）
1. 访问仓库设置页面：
   ```
   https://github.com/YIMUYIGUO/open-curtain-calc/settings/pages
   ```

2. 在"Source"部分：
   - 选择"Deploy from a branch"
   - 分支选择：**main**
   - 文件夹选择：**/ (root)**

3. 点击 **Save** 按钮

4. 等待1-2分钟，GitHub会自动构建和部署

5. 访问您的GitHub Pages：
   ```
   https://yimuyiguo.github.io/open-curtain-calc/
   ```

### 方法二：通过GitHub API（自动）
如果您有API权限，可以使用以下命令启用：

```bash
# 启用GitHub Pages
curl -X POST \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/YIMUYIGUO/open-curtain-calc/pages \
  -d '{
    "source": {
      "branch": "main",
      "path": "/"
    }
  }'
```

### 方法三：通过GitHub CLI
```bash
# 安装GitHub CLI
# 然后运行：
gh repo view YIMUYIGUO/open-curtain-calc --web
# 或者使用API：
gh api repos/YIMUYIGUO/open-curtain-calc/pages \
  -X POST \
  -f source_branch=main \
  -f source_path=/
```

## 📁 文件说明

### 预览文件
1. **preview.html** - 主预览页面
   - 包含项目介绍、特性展示、技术栈、对比表格
   - 响应式设计，支持移动设备
   - 美观的UI和动画效果

2. **preview-demo.sh** - 演示脚本
   - 交互式命令行界面
   - 展示项目启动和功能演示
   - 系统依赖检查

3. **preview-config.yaml** - 预览配置
   - 项目配置信息
   - 功能模块说明
   - 技术栈详情

4. **gh-pages-config.yaml** - GitHub Pages配置
   - Pages设置说明
   - 部署配置
   - 技术支持信息

### 核心项目文件
- **README.md** - 项目详细文档
- **LICENSE** - MIT许可证
- **ROADMAP.md** - 开发路线图
- **backend/** - 后端源码
- **frontend/** - 前端源码
- **docker/** - Docker配置
- **scripts/** - 部署脚本

## 🌐 访问方式

### 已上传的链接
1. **GitHub仓库主页**：
   ```
   https://github.com/YIMUYIGUO/open-curtain-calc
   ```

2. **预览页面（GitHub文件）**：
   ```
   https://github.com/YIMUYIGUO/open-curtain-calc/blob/main/preview.html
   ```
   （点击"Raw"查看原始HTML，或右键"另存为"下载）

3. **GitHub Pages（启用后）**：
   ```
   https://yimuyiguo.github.io/open-curtain-calc/
   ```

### 本地预览
如果您想本地预览：
```bash
# 1. 下载预览文件
wget https://raw.githubusercontent.com/YIMUYIGUO/open-curtain-calc/main/preview.html

# 2. 用浏览器打开
open preview.html  # macOS
start preview.html # Windows
xdg-open preview.html # Linux
```

## ⚙️ 自定义配置

### 修改预览页面
如果您想自定义预览页面：
1. 编辑 `preview.html` 文件
2. 更新样式、内容或功能
3. 重新上传到GitHub

### 添加更多页面
您可以添加更多HTML页面：
```html
<!-- 创建新页面，如demo.html -->
<!DOCTYPE html>
<html>
<head>
    <title>OpenCurtainCalc Demo</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- 页面内容 -->
</body>
</html>
```

### 配置自定义域名
如果您有自己的域名：
1. 在域名DNS中添加CNAME记录：
   ```
   your-domain.com CNAME yimuyiguo.github.io
   ```

2. 在GitHub Pages设置中添加自定义域名

## 🛠️ 故障排除

### 常见问题

**Q: GitHub Pages没有自动构建**
A: 检查仓库设置 → Pages，确保已正确配置分支和文件夹。

**Q: 页面显示404错误**
A: 
1. 等待几分钟，GitHub Pages可能需要时间构建
2. 检查文件名是否正确（区分大小写）
3. 确保文件在仓库根目录

**Q: 样式或图片不显示**
A:
1. 检查CSS和图片路径是否正确
2. 确保使用相对路径或完整URL
3. 清除浏览器缓存

**Q: 如何更新页面**
A:
1. 修改HTML文件
2. 提交更改到GitHub
3. GitHub会自动重新部署（可能需要几分钟）

### 调试工具
1. **GitHub Actions日志**：
   ```
   https://github.com/YIMUYIGUO/open-curtain-calc/actions
   ```

2. **Pages构建状态**：
   ```
   https://github.com/YIMUYIGUO/open-curtain-calc/deployments
   ```

3. **浏览器开发者工具**：
   - 按F12打开
   - 查看Console和Network标签

## 📈 进阶功能

### 添加分析
在 `preview.html` 中添加Google Analytics：
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### 添加SEO优化
```html
<meta name="description" content="OpenCurtainCalc - 开源、智能、高效的幕墙计算系统">
<meta name="keywords" content="幕墙计算,开源软件,结构计算,建筑软件,BIM,AI辅助设计">
<meta property="og:title" content="OpenCurtainCalc">
<meta property="og:description" content="开源幕墙计算系统">
<meta property="og:image" content="https://yimuyiguo.github.io/open-curtain-calc/preview-image.png">
```

### 添加交互功能
```javascript
// 在preview.html中添加JavaScript交互
document.addEventListener('DOMContentLoaded', function() {
    // 添加点击事件
    document.querySelectorAll('.feature-card').forEach(card => {
        card.addEventListener('click', function() {
            alert('功能详情: ' + this.querySelector('.feature-title').textContent);
        });
    });
});
```

## 📞 支持

如果您遇到问题：
1. 查看本指南
2. 检查GitHub Issues
3. 提交新的Issue
4. 联系维护者

## 🔄 更新日志

### 2024-03-24
- ✅ 创建预览页面文件
- ✅ 上传到GitHub仓库
- 📝 编写启用指南
- ⚙️ 准备GitHub Pages配置

### 下一步计划
- [ ] 启用GitHub Pages
- [ ] 添加更多演示内容
- [ ] 完善移动端适配
- [ ] 添加多语言支持

---

**💡 提示**: 启用GitHub Pages后，您的预览页面将可以通过专业URL访问，提升项目展示效果！