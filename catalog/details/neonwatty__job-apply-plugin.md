# neonwatty/job-apply-plugin

AI-powered job application assistant for Claude Code and Codex - fills LinkedIn, Greenhouse, Ashby, and Workday applications

## requirements

Choose either supported host:

- **Codex**: Codex CLI or the Codex desktop app, with the Browser plugin enabled for visible navigation, form filling, authenticated Chrome sessions when selected, and local file uploads
- **Claude Code**: [Claude Code](https://claude.ai/code) with [Claude in Chrome](https://chromewebstore.google.com/detail/claude-in-chrome)

Codex stays inside its selected Browser plugin surface. Claude Code does not require Playwright; an already-configured Playwright integration may be used only for one inaccessible iframe or custom control.

## tools

The examples below use Codex syntax. In Claude Code, replace the leading `$` with `/`.

## installation

1. Invoke the skill:
   ```
   $job-apply:job-apply
   ```

2. Provide your resume path when prompted:
   ```
   ~/Documents/resume.pdf
   ```

3. Review and confirm extracted profile information

## features

- **Never handles credentials** - Pauses for you to complete login, password, CAPTCHA, or MFA steps
- **Never creates accounts** - Pauses so you can decide whether to create an account yourself
- **Never submits applications** - Stops at final review, summarizes entered fields, and leaves Submit or Send for you
- **Never enters payment info** - Skips premium features
- **Confirms sensitive questions** - Salary, visa status, etc.
- **Separates use from storage consent** - Filling a sensitive answer once never automatically remembers it
