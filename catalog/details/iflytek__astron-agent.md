# iflytek/astron-agent

Enterprise-grade, commercial-friendly agentic workflow platform for building next-generation SuperAgents.

## features

- **Stable and Reliable**: Built on the same core technology as the iFLYTEK Astron Agent Platform, providing enterprise-grade reliability with a fully available high-availability version open source.
- **Cross-System Integration**: Natively integrates intelligent RPA, efficiently connecting internal and external enterprise systems, enabling seamless interaction between Agents and enterprise systems.
- **Enterprise-Grade Open Ecosystem**: Deeply compatible with various industry models and tools, supporting custom extensions and flexibly adapting to diverse enterprise scenarios.
- **Business-Friendly**: Released under the Apache 2.0 License, with no commercial restrictions, allowing free commercial use.

### Key Features
- **Enterprise-Grade High Availability:** Full-stack capabilities for development, building, optimization, and management. Supports one-click deployment with strong reliability.  
- **Intelligent RPA Integration:** Enables cross-system process automation, empowering Agents with controllable execution to achieve a complete loop “from decision to action.”  
- **Ready-to-Use Tool Ecosystem:** Integrates massive AI capabilities and tools from the [iFLYTEK Open Platform](https://www.xfyun.cn), validated by millions of developers, supporting plug-and-play integration without extra development.  
- **Flexible Large Model Support:** Offers diverse access methods, from rapid API-based model access and validation to one-click deployment of enterprise-level MaaS (Model as a Service) on-premises clusters, meeting needs of all scales.  

## 🤝 [Adopters](https://iflytek.github.io/astron-agent/cases/)

<div align="center">

<img src="./docs/cases/imgs/donghua.png" alt="东华软件" height="56" />&nbsp;&nbsp;&nbsp;&nbsp;
<img src="./docs/cases/imgs/chinatelecom.png" alt="中国电信" height="56" />&nbsp;&nbsp;&nbsp;&nbsp;
<img src="./docs/cases/imgs/yunsuan.jpg" alt="云算数字科技" height="56" />&nbsp;&nbsp;&nbsp;&nbsp;
<img src="./docs/cases/imgs/xiaoqu.png" alt="小趣科技" height="56" />&nbsp;&nbsp;&nbsp;&nbsp;
<img src="./docs/cases/imgs/shandongyungu.png" alt="山东云谷" height="56" />
<br/><br/>
<img src="./docs/cases/imgs/guangwu.jpg" alt="广物互联" height="56" />&nbsp;&nbsp;&nbsp;&nbsp;
<img src="./docs/cases/imgs/yugou.jpg" alt="北京榆构" height="56" />&nbsp;&nbsp;&nbsp;&nbsp;
<img src="./docs/cases/imgs/fiberhome.png" alt="烽火通信" height="56" />&nbsp;&nbsp;&nbsp;&nbsp;
<img src="./docs/cases/imgs/foxit.jpg" alt="厦门福昕中数" height="56" />&nbsp;&nbsp;
<img src="./docs/cases/imgs/xiangyang-dongsheng.png" alt="襄阳东昇" height="28" />

</div>

## 📰 News

### 🔄 Ongoing

### 📅 Past

- **[Astron Hackathon @ 2025 iFLYTEK Global 1024 Developer Festival](https://luma.com/9zmbc6xb)**  🎤 <a href="https://github.com/mklong"><img src="https://github.com/mklong.png" width="20" align="center" /> @mklong</a>
- **[Astron Agent Zhengzhou Meetup](https://github.com/iflytek/astron-agent/discussions/672)**  🎤 <a href="https://github.com/lyj715824"><img src="https://github.com/lyj715824.png" width="20" align="center" /> @lyj715824</a> <a href="https://github.com/wowo-zZ"><img src="https://github.com/wowo-zZ.png" width="20" align="center" /> @wowo-zZ</a>
- **[Astron on Campus @ Zhejiang University of Finance and Economics](https://mp.weixin.qq.com/s/oim_Z0ckgpFwf5jOskoJuA)**  🎤 <a href="https://github.com/lyj715824"><img src="https://github.com/lyj715824.png" width="20" align="center" /> @lyj715824</a>
- **[Astron Agent & RPA · Qingdao Meetup Brings Agentic AI!](https://github.com/iflytek/astron-agent/discussions/740)**  🎤 <a href="https://github.com/vsxd"><img src="https://github.com/vsxd.png" width="20" align="center" /> @vsxd</a> <a href="https://github.com/doctorbruce"><img src="https://github.com/doctorbruce.png" width="20" align="center" /> @doctorbruce</a> <a href="https://github.com/MaxwellJean"><img src="https://github.com/MaxwellJean.png" width="20" align="center" /> @MaxwellJean</a>
- **[Astron Training Camp · Cohort #1](https://www.aidaxue.com/astronCamp)**  🎤 <a href="https://

## installation

We offer two deployment methods to meet different scenarios:

### Option 1: Docker Compose (Recommended for Quick Start)

```bash
# Clone the repository
git clone https://github.com/iflytek/astron-agent.git

# Navigate to the Docker deployment directory
cd docker/astronAgent

## configuration

cp .env.example .env

# Configure environment variables
vim .env
```

For environment variable configuration, please refer to the documentation:[DEPLOYMENT_GUIDE_WITH_AUTH.md](https://github.com/iflytek/astron-agent/blob/main/docs/DEPLOYMENT_GUIDE_WITH_AUTH.md#step-2-configure-astronagent-environment-variables)

```bash
# Start all services (including Casdoor)
docker compose -f docker-compose-with-auth.yaml up -d
```

#### 📊 Service Access Addresses

After startup, you can access the services at the following addresses:

**Authentication Service**
- **Casdoor Admin Interface**: http://localhost:8000

**AstronAgent**
- **Application Frontend (nginx proxy)**: http://localhost/

**Note**
- Default Casdoor login credentials: username: `admin`, password: `123`

### Option 2: Helm (For Kubernetes Environments)

> 🚧 **Note**: Helm charts are currently under development. Stay tuned for updates!

```bash
# Coming soon
# helm repo add astron-agent https://iflytek.github.io/astron-agent
