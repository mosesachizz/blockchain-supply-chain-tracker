"""
Metrics collection for blockchain operations.
"""

import boto3
from typing import Dict
from ..utils.logger import setup_logger

class MetricsCollector:
    """Collects and sends metrics to CloudWatch (or console for local)."""
    
    def __init__(self):
        """Initialize metrics collector."""
        self.logger = setup_logger(__name__)
        self.cloudwatch = boto3.client("cloudwatch", region_name="us-east-1") if os.getenv("AWS_REGION") else None
        self.namespace = "SupplyChainTracker"

    def record_event_logged(self):
        """Record a supply chain event log."""
        self._put_metric("EventsLogged", 1)

    def record_query_success(self):
        """Record a successful query."""
        self._put_metric("QueriesSuccess", 1)

    def record_error(self):
        """Record an error."""
        self._put_metric("Errors", 1)

    def _put_metric(self, metric_name: str, value: int):
        """Send metric to CloudWatch or log locally.
        
        Args:
            metric_name (str): Name of the metric.
            value (int): Metric value.
        """
        try:
            if self.cloudwatch:
                self.cloudwatch.put_metric_data(
                    Namespace=self.namespace,
                    MetricData=[{
                        "MetricName": metric_name,
                        "Value": value,
                        "Unit": "Count"
                    }]
                )
            else:
                self.logger.debug("Local metric %s: %d", metric_name, value)
        except Exception as e:
            self.logger.error("Failed to record metric %s: %s", metric_name, str(e))