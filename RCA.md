
# Incident Report: High CPU Usage Spike

## Summary
A high CPU usage spike was observed in the monitored system during runtime, triggering the configured alert in Grafana.

---

## ⏱ Timeline
- T0: System running under normal load (~2% CPU)
- T1: Load simulation initiated using multiple `yes` processes
- T2: CPU usage exceeded 5%
- T3: Alert entered Pending state
- T4: Alert transitioned to FIRING after 1 minute
- T5: Processes terminated
- T6: System recovered to normal state

---

## Root Cause
The CPU spike was caused by multiple concurrent infinite loop processes:

```bash
yes > /dev/null &
````

These processes continuously consumed CPU resources without termination.

---

## Detection

* Metric: CPU Usage
* Tool: Prometheus + Grafana
* Alert condition:

        CPU > 5% for 1 minute

The issue was detected using a Grafana alert based on CPU usage.

CPU metric:

100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[1m])) * 100)

---

## 🛠 Resolution

* Identified running processes using system monitoring
* Terminated processes using:

```bash
killall yes
```

---

## Recovery

System CPU usage returned to baseline (~2%) and alert state transitioned back to Normal.

---

## Learnings

* Importance of threshold-based alerting
* Need for sustained-condition detection (not spikes)
* Understanding system behavior under artificial load

---

## Preventive Measures

* Tune alert thresholds based on system baseline
* Add process-level monitoring
* Implement auto-remediation scripts (future work)

````

---
