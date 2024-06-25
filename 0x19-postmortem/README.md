## Postmortem: Web Stack Outage on E-commerce Platform
### Issue Summary
**Duration of Outage:**
June 5, 2024, 14:30 UTC - June 5, 2024, 15:45 UTC (1 hour, 15 minutes)
**Impact:**
The e-commerce website was completely inaccessible. Customers needed help browsing products, placing orders, or accessing their accounts. Approximately 85% of users were affected, leading to significant disruption in sales and customer service operations.
**Root Cause:**
A misconfiguration in the load balancer settings failed to distribute traffic correctly, leading to server overload and eventual crash.
### Timeline
- **14:30 UTC:** Issue detected by automated monitoring system, which reported high latency and timeout errors.
- **14:32 UTC:** The on-call engineer received an alert via SMS and email.
- **14:35 UTC:** Initial investigation began; logs indicated potential overload on web servers.
- **14:40 UTC:** Misleading path: Suspected DDoS attack; started implementing mitigation strategies.
- **14:50 UTC:** Escalation to the network operations team for deeper analysis.
- **15:00 UTC:** The network team discovered no signs of an external attack; the focus shifted back to internal configuration.
- **15:10 UTC:** Load balancer logs reviewed; misconfiguration identified.
- **15:15 UTC:** Configuration corrected; traffic distribution normalized.
- **15:20 UTC:** Gradual recovery observed as servers stabilized.
- **15:45 UTC:** Full service was restored, and monitoring continued to ensure stability.
### Root Cause and Resolution
**Root Cause:**
The root cause was a misconfiguration in the load balancer settings during a recent update. The settings incorrectly routed all incoming traffic to a single web server instead of distributing it across multiple servers. This led to server overload and subsequent crashes, rendering the website inaccessible.
**Resolution:**
The load balancer configuration was corrected to ensure proper traffic distribution across all web servers. Specifically, the round-robin setting was reinstated, and the weight parameters were adjusted to balance the load evenly. After applying these changes, the web servers began handling traffic as expected, and the website's performance returned to normal.
### Corrective and Preventative Measures
**Improvements and Fixes:**
- Conduct a thorough review of all configuration changes in a staging environment before deployment.
- Implement additional monitoring on load balancers to detect configuration anomalies.
- Enhance alerting systems to distinguish between internal misconfigurations and external threats, such as DDoS attacks.
**Tasks:**
1. **Update Configuration Management Process:**
 - Create detailed documentation for load balancer settings and update procedures.
 - Implement a checklist for configuration changes that includes a peer review step.
2. **Enhance Monitoring and Alerts:**
 - Add specific alerts for unusual traffic patterns and server load.
 - Set up automated health checks for load balancers to verify proper traffic distribution.
3. **Training and Knowledge Sharing:**
 - Conduct training sessions for the operations team on the importance of load balancer configurations.
 - Share this postmortem with the entire engineering team to prevent similar issues in the future.
4. **Conduct Regular Audits:**
 - Schedule regular audits of critical system configurations to ensure compliance with best practices.
 - Use automated tools to check for configuration drift and notify the team of any discrepancies.
By addressing these corrective and preventative measures, we aim to improve our system's resilience and reduce the likelihood of similar incidents occurring in the future. This incident underscores the importance of meticulous configuration management and the value of robust monitoring systems.
