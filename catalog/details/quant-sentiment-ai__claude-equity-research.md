# quant-sentiment-ai/claude-equity-research

🔌 Claude Code Plugin for institutional-grade equity research. Install with /plugin marketplace add. Generates professional buy/sell recommendations with comprehensive fundamental analysis, technical i

## features

- **Institutional-Grade Analysis**: Generates professional equity research reports matching Wall Street standards
- **AI-Powered Intelligence**: Leverages Claude AI for comprehensive fundamental and technical analysis
- **Real-Time Data Integration**: Pulls live market data, earnings reports, and analyst coverage
- **Risk-Adjusted Recommendations**: Provides buy/sell/hold ratings with specific price targets and position sizing
- **Advanced Market Intelligence**: Includes options flow analysis, insider trading activity, and sector positioning

## Key Features

### Core Analysis Framework
- **Executive Summary**: Investment thesis with price target and 12-month timeframe
- **Fundamental Analysis**: Revenue growth, margins, peer comparisons, and forward estimates
- **Catalyst Analysis**: Near-term and medium-term market drivers with specific dates
- **Valuation Models**: Bull/base/bear scenarios with probability weighting
- **Risk Assessment**: Company-specific and macro risks with position sizing guidance (1-5%)
- **Technical Context**: Support/resistance levels, momentum indicators, and volume analysis

### Enhanced Intelligence Features
- **Options Flow Analysis**: Unusual activity, put/call ratios, implied volatility trends
- **Insider Activity Monitoring**: Executive buying/selling patterns with dollar amounts
- **Sector Positioning**: Rotation trends and relative strength vs market indices
- **ESG & Governance**: Sustainability scores and regulatory compliance assessment

### Professional Standards
- **Institutional Terminology**: EBITDA, P/E ratios, EV/Sales, conviction levels
- **Probability Weighting**: Bull/base/bear scenarios with percentage allocations
- **Legal Protection**: Comprehensive disclaimers for educational use
- **Data Sourcing**: Real-time web search with analyst firm citations

## requirements

- Claude Code CLI (version 2.0.11 or higher)
- Claude paid subscription (Pro, Team, or Enterprise)
- Internet connection for real-time data retrieval

## installation

**Quick Install - Interactive Menu:**
```bash
# Step 1: Add the marketplace
/plugin marketplace add quant-sentiment-ai/claude-equity-research

# Step 2: Open the plugin menu
/plugin

# Step 3: Select "Browse Plugins" → find "claude-equity-research" → "Install now"
```

**Alternative - Direct Install:**
```bash
/plugin marketplace add quant-sentiment-ai/claude-equity-research
/plugin install trading-ideas@claude-equity-research-marketplace
```

**Verify Installation:**
```bash
/help  # Confirm /trading-ideas:research command is listed
```

**Start Analyzing:**
```bash
/trading-ideas:research AAPL
/trading-ideas:research NVDA --detailed
```

> Claude Code namespaces plugin commands as `<plugin-name>:<command-name>`, so the invocation is `/trading-ideas:research` (not the bare `/trading-ideas`). If you prefer the bare form, use the [manual install](#manual-installation-advanced) below — it copies the command file into your personal `~/.claude/commands/` and registers it as `/trading-ideas`.

> 💡 **Tip**: Restart Claude Code after installation for best results.

For comprehensive plugin documentation, see [PLUGIN.md](PLUGIN.md).

<details>
<summary><strong>Manual Installation (Advanced)</strong></summary>

### Quick Start

1. **Install the /trading-ideas command** (system-wide):
```bash
mkdir -p ~/.claude/commands
curl -o ~/.claude/commands/trading-ideas.md https://raw.githubusercontent.com/quant-sentiment-ai/claude-equity-research/main/commands/trading-ideas/commands/research.md
```

2. **Basic usage**:
```bash
/trading-ideas AAPL
```

3. **Enhanced analysis**:
```bash
/trading-ideas HOOD --detailed
```

### Manual Setup via Git Clone

1. **Clone the repository**:
```bash
git clone https://github.com/quant-sentiment-ai/claude-equity-research.git
cd claude-equity-research
```

2. **Copy command to Claude Code**:
```bash
cp commands/trading-ideas/commands/research.md ~/.claude/commands/trading-ideas.md
```

</details>

## tools

> Examples below use the plugin install invocation (`/trading-ideas:research`). If you followed the manual install path, drop the `:research` suffix and use the bare `/trading-ideas` form.

### Basic Equity Analysis
```bash
/trading-ideas:research AAPL
```
**Output**: Comprehensive institutional research report with BUY/SELL/HOLD recommendation

### Technology Sector Analysis
```bash
/trading-ideas:research NVDA
```
**Features**: AI/semiconductor sector positioning, relative valuation vs peers

### Financial Services Analysis
```bash
/trading-ideas:research JPM
```
**Includes**: Interest rate sensitivity, regulatory environment, book value analysis

### Growth Stock Analysis
```bash
/trading-ideas:research TSLA
```
**Focus**: Growth metrics, competitive positioning, volatility assessment

## Sample Output Format

```
# APPLE INC (AAPL) - ENHANCED EQUITY RESEARCH

## EXECUTIVE SUMMARY
BUY with $250 price target (9% upside) over 12 months. Strong Q4 2024 
results driven by iPhone 16 launch and AI integration provide foundation 
for premium product cycle. Balanced risk-reward with established ecosystem moat.

## FUNDAMENTAL ANALYSIS
Q4 2024: Revenue $94.9B (+6% YoY), EPS $1.64 (+12% YoY). iPhone revenue 
$46.2B (~49% of total), Services +12% to $25B with recurring characteristics.

## VALUATION & PRICE TARGETS
Consensus: $242 (range $200-$280)
Bull case: $280 | Base case: $250 | Bear case: $200
Probability weighting: 25%/55%/20%

## RECOMMENDATION: BUY | Conviction: High | Price Target: $250
```

## Command Reference

| Command | Description | Output |
|---------|-------------|---------|
| `/trading-ideas:research <TICKER>` | Standard institutional analysis | 8-section comprehensive report |
| `/trading-ideas:research <TICKER> --detailed` | Enhanced analysis with options flow | Extended technical and insider analysis |
| `/trading-ideas:research --help` | Show usage information | Command documentation |

## Repository Structure

```
claude-equity-research/
├── README.md                     # This file
├── LICENSE                       # MIT License
├── commands/
│   ├── trading-ideas/            # Plugin directory (installed via marketplace)
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json       # Plugin manifest
│   │   └── commands/
│   │       └── research.md       # Slash command (invoked as /trading-ideas:research)
│   └── README.md                 # Command documentation
├── config/
│   ├── config.example.json       # Template configuration
│   └── prompts/                  # Analysis prompt templates
├── examples/
│   └── sample_reports/           # Example analyses (AAPL, HOOD, etc.)
├── docs/
│   ├── methodology.md            # Detailed analysis framework
│   ├── installation.md           # Setup instructions
│   └── customization.md          # Customization guide
├── utils/
│   ├── data_sources.md           # Data source documentation
│   └── validation.py             # Analysis validation tools
└── tests/
    └── test_command.py           # Command functionality tests
```

## Analysis Methodology

Our research framework combines:

### Quantitative Analysis
- **Financial Statements**: Revenue, margins, cash flow analysis
- **Valuation Models**: Multiple approaches (DCF, comparable company, precedent transaction)
- **Technical Indicators**: Support/resistance, momentum, relative strength
- **Options Analytics**: Implied volatility, unusual activity, sentiment indicators

### Qualitative Assessment
- **Competitive Positioning**: Market share, competitive advantages, moat analysis
- **Management Quality**: Track record, capital allocation, strategic vision
- **Regulatory Environment**: Industry-specific risks, compliance issues
- **ESG Factors**: Environmental, social, governance considerations

### Risk Management
- **Scenario Analysis**: Bull/base/bear cases with probability weighting
- **Position Sizing**: Risk-adjusted allocation recommendations (1-5% typical)
- **Stop-Loss Guidance**: Downside protection levels
