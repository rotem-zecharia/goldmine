# xbtlin/ai-berkshire

AI 时代的伯克希尔：基于 Claude Code / Codex 的价值投资研究框架。巴菲特·芒格·段永平·李录四大师方法论 + 多Agent并行研究。/ AI-era Berkshire: a value investing research framework built for Claude Code / Codex. 4 masters' methodologies + multi-ag

## tools

cd ai-berkshire
./scripts/install-claude-commands.sh
```

Claude Code 用户安装（Windows PowerShell / Command Prompt）：

```bat
git clone https://github.com/xbtlin/ai-berkshire.git
cd ai-berkshire
.\scripts\install-claude-commands.bat
```

Codex 用户安装（macOS / Linux）：

```bash
# 克隆仓库
git clone https://github.com/xbtlin/ai-berkshire.git

# 生成并安装 Codex skills 到 ~/.codex/skills
cd ai-berkshire
./scripts/install-codex-skills.sh

# 可选：安装 Codex slash prompts 到 ~/.codex/prompts
# 用于获得接近 Claude Code 的 /investment-research 体验
./scripts/install-codex-prompts.sh
```

Codex 用户安装（Windows PowerShell / Command Prompt）：

```bat
git clone https://github.com/xbtlin/ai-berkshire.git
cd ai-berkshire
.\scripts\install-codex-skills.bat

REM 可选：安装 Codex slash prompts
.\scripts\install-codex-prompts.bat
```

仓库同时维护三套入口：`skills/*.md` 是 Claude Code command 源文件；`codex-skills/*/SKILL.md` 是 Codex skill 包，由 `scripts/sync-codex-skills.py` 从 `skills/*.md` 生成；`codex-prompts/*.md` 是可选的 Codex slash prompt 兼容层。

### 3. 使用

在 Claude Code 中直接调用：

```bash
# 深度研究
/investment-research 腾讯
/investment-team 美团
/management-deep-dive 王兴 美团
/private-company-research SpaceX
/deep-company-series 拼多多

# 财报分析
/earnings-review 腾讯 2025Q4
/earnings-team PDD 2025年报

# 行业筛选
/industry-research 核电
/industry-funnel AI算力
/quality-screen 恒生指数成分股
/bottleneck-hunter AI基础设施
/investment-checklist 茅台, 英伟达, 苹果

# 持仓管理
/income-investment Verizon mode=existing role=core-income quantity=100 cost_basis=39.50 tax_residence=France horizon=5y
/portfolio-review 腾讯30%, 美团20%, 茅台20%, 现金30%
/thesis-tracker 拼多多
/thesis-drift 拼多多 reports/拼多多-thesis-2025Q4.md reports/拼多多-thesis-2026Q1.md
/news-pulse 腾讯

# 思维工具
/dyp-ask 拼多多的护城河到底在哪里？
/wechat-article 美团
```

在 Codex 中安装后重启 Codex，然后直接按 skill 名称描述任务，例如：

```text
使用 investment-research 研究腾讯
使用 earnings-review 分析 PDD 2025年报
使用 industry-funnel 筛选 AI算力
使用 bottleneck-hunter 扫描 AI基础设施瓶颈
使用 thesis-drift 对比拼多多两份投资论文
使用 wechat-article 写美团投研文章
```

如果安装了 Codex slash prompts，重启 Codex 后也可以在 `/` 菜单里搜索这些 prompt。Codex 官方的 custom prompt 入口通常显示为 `prompts:<name>`，例如：

```text
/prompts:investment-research 腾讯
```

---

## 各 Skill 详细介绍

### 1. `/investment-research` — 四大师综合分析

最全面的单公司深度研究框架。按七个模块顺序执行：

```
数据收集 → 生意本质(段永平) → 护城河(巴菲特) → 逆向思考(芒格)
    → 管理层评估(段永平+巴菲特) → 文明趋势(李录) → 估值与安全边际
```

**核心特色**：
- AI研究偏见自觉机制（A/B/C级信息丰富度评级）
- 关键数据多源交叉验证（市值手算校验、至少2个独立来源）
- 四位大师的"追问"贯穿全文
- 三情景估值（乐观/中性/悲观）+ 反向DCF

**输出示例摘录**：

> #### 综合决策备忘录
>
> | 维度 | 结论 | 信心度 |
> |------|------|--------|
> | 生意质量（段永平） | 极佳：平台型生意，双边网络效应，边际成本趋零 | ★★★★★ |
> | 护城河（巴菲特） | 宽阔且在变宽：网络效应+转换成本+规模效应三重叠加 | ★★★★☆ |
> | 管理层（段永平+巴菲特） | 优秀：创始人掌舵，资本配置纪律强 | ★★★★☆ |
> | 最大风险（芒格） | 监管政策不确定性，新业务亏损拖累整体利润 | ★★★☆☆ |
> | 文明趋势（李录） | 顺应数字化消费趋势，但非"文明级范式转移" | ★★★★☆ |
> | 估值（巴菲特+段永平） | 当前PE 18x，处于历史中位数偏低，有一定安全边际 | ★★★★☆ |
>
> **段永平**："这门生意的本质是连接消费者和商家，赚的是效率提升的钱。好生意的标志是：用户越多，商家越多；商家越多，用户越多。飞轮一旦转起来，很难停下。"
>
> **芒格**："反过来想——如果这家公司明天消失，用户和商家会怎么办？如果答案是'很快找到替代品'，那护城河就不够深。如果答案是'生活会变得非常不方便'，那就值得关注。"

---

### 2. `/investment-team` — 多Agent投研团队

启动4个AI Agent并行研究，模拟真实投研团队协作。每个Agent独立搜索、独立分析、独立给出评分，最后由Team Lead综合研判。

**输出示例摘录**：

> #### 一句话结论
> 美团是中国本地生活服务的绝对龙头，拥有多重网络效应护城河，当前估值处于历史较低水平，长期投资价值显著，建议逢低建仓。
>
> #### 四维评分总表
>
> | 维度 | 框架 | 评分 | 核心判断 |
> |------|------|------|----------|
> | 商业模式 & 护城河 | 段永平 | ★★★★☆ | 双边网络效应强劲，外卖+到店形成飞轮 |
> | 财务 & 估值 | 巴菲特 | ★★★★☆ | 核心业务利润率持续改善，估值处于历史低位 |
> | 行业 & 竞争 | 芒格 | ★★★☆☆ | 抖音入侵到店业务，竞争格局有恶化风险 |
> | 风险 & 管理层 | 李录 | ★★★★☆ | 王兴战略眼光出色，但新业务烧钱需警惕 |
>
> **综合评分：3.8 / 5**
>
> #### 投资建议
>
> | 策略 | 建议 | 价格区间(港元) |
> |------|------|---------------|
> | 激进型 | 当前价位可建仓30% | 120-140 |
> | 稳健型 | 等回调至100-110建仓 | 100-120 |
> | 保守型 | 等待季报验证利润率趋势后再介入 | <100 |

---

### 3. `/investment-checklist` — 巴菲特买入前 Checklist

六关快速筛选，帮你在10分钟内决定一家公司是否值得深入研究：

```
第一关：能力圈（我能理解吗？）
    ↓ 通过
第二关：好生意（经济特征如何？）
    ↓ 通过
第三关：护城河（竞争优势深不深？）
    ↓ 通过
第四关：管理层（值得信任吗？）
    ↓ 通过
第五关：安全边际（价格便宜吗？）
    ↓ 通过
第六关：决策纪律（是理性还是FOMO？）
    ↓ 通过
   ✅ 镜子测试
```

**支持多公司对比**——一次筛选多个标的：

```
/investment-checklist 腾讯, 阿里巴巴, 美团, 拼多多
```

**输出示例摘录**：

> #### 镜子测试
>
> "我以 380港元 买入 腾讯，因为：
> 1. 
