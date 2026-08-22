# databasus/databasus

PostgreSQL backup tool with Point-In-Time-Recovery and restore verification

## installation

You have four ways to install Databasus:

- Automated script (recommended)
- Simple Docker run
- Docker Compose setup
- Kubernetes with Helm

<img src="assets/healthchecks.svg" alt="Databasus Dashboard" width="800"/>

---

## tools

1. **Access the dashboard**: Navigate to `http://localhost:4005`
2. **Add your first database for backup**: Click "New Database" and follow the setup wizard
3. **Configure schedule**: Choose from hourly, daily, weekly, monthly or cron intervals
4. **Set database connection**: Enter your database credentials and connection details
5. **Choose storage**: Select where to store your backups (local, S3, Google Drive, etc.)
6. **Configure retention policy**: Choose time period, count or GFS to control how long backups are kept
7. **Add notifications** (optional): Configure email, Telegram, Slack, Mattermost or webhook notifications
8. **Save and start**: Databasus will validate settings and begin the backup schedule
