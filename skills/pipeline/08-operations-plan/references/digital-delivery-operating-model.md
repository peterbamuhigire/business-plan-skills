Parent: [Operations Plan Skill](../SKILL.md)

When to read: when the business sells software, runs SaaS, a digital platform, managed IT, app development, hosting, cloud migration, or technology-enabled operations, and the plan must describe how digital services are delivered reliably.

# Digital Delivery Operating Model

DevOps is a business operating model for delivering digital services reliably, not a tool list. This reference paraphrases practice from *Strategic DevOps*; *DevOps for PHP Developers*; Kim, G. et al. *The DevOps Handbook*, 2nd edn, IT Revolution; and *Modern DevOps Practices* (confirm remaining author and publisher details before citing). Tool and platform recommendations change quickly; verify current versions and support status before naming a product.

## 1. Translate capability into business outcomes

Describe DevOps in the plan as:

- shorter time from feature idea to customer value;
- lower release risk through automation, tests, rollback, and staged rollout;
- better service reliability through monitoring, incident response, and recovery;
- more customer trust through fewer outages and clear maintenance notices;
- lower hidden cost through less manual deployment, rework, and unplanned support.

## 2. Capabilities to describe

| Capability | Plan wording |
|---|---|
| Continuous integration and delivery pipeline | Repeatable process that builds, tests, and promotes software through environments |
| Release management | Controlled rollout, release notes, change records, rollback triggers, post-release monitoring |
| Observability | Dashboards, alerts, logs, metrics, and traces for customer-facing services |
| Incident response | Severity levels, on-call owner, escalation path, status updates, post-incident learning |
| Infrastructure as code | Version-controlled environment setup that prevents configuration drift |
| Security in delivery | Dependency checks, secret handling, vulnerability scanning, least-privilege deployment access |
| Cloud-native operations | Containers, orchestration, autoscaling, health checks, environment separation — only where justified |

## 3. Measures

Deployment frequency; lead time for changes; change failure rate; time to restore service; availability; error rate and latency on critical journeys; incident count and severity; support tickets caused by defects or downtime; cloud cost per user, tenant, transaction, or workload; pipeline duration and manual release effort.

## 4. Maturity path (avoid overbuilding)

1. **Basic discipline:** version control, backups, staging environment, documented deployment, manual smoke tests.
2. **Controlled delivery:** automated checks, repeatable deployment, release notes, rollback plan, monitoring.
3. **Scalable delivery:** artefact promotion, automated tests, infrastructure as code, blue-green or canary releases, observability, incident reviews.
4. **Cloud-native scale:** containers, managed orchestration platforms, GitOps, service-level objectives, security built into delivery, cost allocation.

Do not recommend Kubernetes, microservices, or GitOps unless scale, reliability needs, team maturity, or deployment complexity justify them. State the current stage and the trigger for moving to the next.

## 5. Financial and plan links

- **Staff plan:** developers, platform or DevOps engineer, QA, support and on-call roles.
- **Cost plan:** hosting, monitoring, build runners, backup storage, security tools, domains and certificates, incident communication tools. Check current prices; do not copy book-era figures.
- **Implementation timeline:** staging environment, pipeline, monitoring, backup-and-restore test, and release process in place before public launch.
- **Risk:** downtime, failed releases, security incidents, cloud cost overrun, vendor lock-in, key-person dependency.
- **Funding request:** present infrastructure as risk reduction and revenue protection, not generic IT spend.

## 6. PHP and LAMP/WAMP businesses

Include: managed environment variables and secrets; Composer dependency discipline; ownership of PHP-FPM or runtime configuration; database backup and migration process; OPcache and cache clear-and-warm procedure; queue-worker process control; file-upload storage and restore; server update and security-patch policy.

## 7. Anti-patterns

- "We will use DevOps" without naming the delivery process.
- Budgeting only for features while omitting hosting, monitoring, backup, support, and release operations.
- Claiming enterprise reliability with no incident response or rollback.
- Proposing advanced cloud-native tooling before basic delivery discipline exists.
- Treating security as an annual audit rather than a check inside delivery.

For deeper engineering standards, route to the engineering catalogue engine (`chwezi-dev-engine`) through the global routing table.
