#!/usr/bin/env python
# -*- coding: utf-8
from __future__ import absolute_import

import datetime

import six

from k8s.base import Model
from k8s.fields import Field, ListField, RequiredField
from k8s.models.v1_13.apimachinery.apis.meta.v1 import LabelSelector, ListMeta, ObjectMeta


###############################################################################
# This file is auto-generated! Do not edit!
#
# Codestyle checking is disabled for this file
# flake8: noqa
###############################################################################


class MetricValueStatus(Model):
    """
    MetricValueStatus holds the current value for a metric
    """

    averageUtilization = Field(int)
    averageValue = Field(six.text_type)
    value = Field(six.text_type)


class ResourceMetricStatus(Model):
    """
    ResourceMetricStatus indicates the current value of a resource metric known to
    Kubernetes, as specified in requests and limits, describing each pod in the
    current scale target (e.g. CPU or memory).  Such metrics are built in to
    Kubernetes, and have special scaling options on top of those available to
    normal per-pod metrics using the 'pods' source.
    """

    current = RequiredField(MetricValueStatus)
    name = RequiredField(six.text_type)


class MetricTarget(Model):
    """
    MetricTarget defines the target value, average value, or average utilization of
    a specific metric
    """

    averageUtilization = Field(int)
    averageValue = Field(six.text_type)
    type = RequiredField(six.text_type)
    value = Field(six.text_type)


class ResourceMetricSource(Model):
    """
    ResourceMetricSource indicates how to scale on a resource metric known to
    Kubernetes, as specified in requests and limits, describing each pod in the
    current scale target (e.g. CPU or memory).  The values will be averaged
    together before being compared to the target.  Such metrics are built in to
    Kubernetes, and have special scaling options on top of those available to
    normal per-pod metrics using the 'pods' source.  Only one 'target' type should
    be set.
    """

    name = RequiredField(six.text_type)
    target = RequiredField(MetricTarget)


class MetricIdentifier(Model):
    """
    MetricIdentifier defines the name and optionally selector for a metric
    """

    name = RequiredField(six.text_type)
    selector = Field(LabelSelector)


class PodsMetricStatus(Model):
    """
    PodsMetricStatus indicates the current value of a metric describing each pod in
    the current scale target (for example, transactions-processed-per-second).
    """

    current = RequiredField(MetricValueStatus)
    metric = RequiredField(MetricIdentifier)


class PodsMetricSource(Model):
    """
    PodsMetricSource indicates how to scale on a metric describing each pod in the
    current scale target (for example, transactions-processed-per-second). The
    values will be averaged together before being compared to the target value.
    """

    metric = RequiredField(MetricIdentifier)
    target = RequiredField(MetricTarget)


class ExternalMetricStatus(Model):
    """
    ExternalMetricStatus indicates the current value of a global metric not
    associated with any Kubernetes object.
    """

    current = RequiredField(MetricValueStatus)
    metric = RequiredField(MetricIdentifier)


class ExternalMetricSource(Model):
    """
    ExternalMetricSource indicates how to scale on a metric not associated with any
    Kubernetes object (for example length of queue in cloud messaging service, or
    QPS from loadbalancer running outside of cluster).
    """

    metric = RequiredField(MetricIdentifier)
    target = RequiredField(MetricTarget)


class HorizontalPodAutoscalerCondition(Model):
    """
    HorizontalPodAutoscalerCondition describes the state of a
    HorizontalPodAutoscaler at a certain point.
    """

    lastTransitionTime = Field(datetime.datetime)
    message = Field(six.text_type)
    reason = Field(six.text_type)
    status = RequiredField(six.text_type)
    type = RequiredField(six.text_type)


class CrossVersionObjectReference(Model):
    """
    CrossVersionObjectReference contains enough information to let you identify the
    referred resource.
    """

    apiVersion = Field(six.text_type)
    kind = RequiredField(six.text_type)
    name = RequiredField(six.text_type)


class ObjectMetricStatus(Model):
    """
    ObjectMetricStatus indicates the current value of a metric describing a
    kubernetes object (for example, hits-per-second on an Ingress object).
    """

    current = RequiredField(MetricValueStatus)
    describedObject = RequiredField(CrossVersionObjectReference)
    metric = RequiredField(MetricIdentifier)


class MetricStatus(Model):
    """
    MetricStatus describes the last-read state of a single metric.
    """

    external = Field(ExternalMetricStatus)
    object = Field(ObjectMetricStatus)
    pods = Field(PodsMetricStatus)
    resource = Field(ResourceMetricStatus)
    type = RequiredField(six.text_type)


class HorizontalPodAutoscalerStatus(Model):
    """
    HorizontalPodAutoscalerStatus describes the current status of a horizontal pod
    autoscaler.
    """

    conditions = ListField(HorizontalPodAutoscalerCondition)
    currentMetrics = ListField(MetricStatus)
    currentReplicas = RequiredField(int)
    desiredReplicas = RequiredField(int)
    lastScaleTime = Field(datetime.datetime)
    observedGeneration = Field(int)


class ObjectMetricSource(Model):
    """
    ObjectMetricSource indicates how to scale on a metric describing a kubernetes
    object (for example, hits-per-second on an Ingress object).
    """

    describedObject = RequiredField(CrossVersionObjectReference)
    metric = RequiredField(MetricIdentifier)
    target = RequiredField(MetricTarget)


class MetricSpec(Model):
    """
    MetricSpec specifies how to scale based on a single metric (only `type` and one
    other matching field should be set at once).
    """

    external = Field(ExternalMetricSource)
    object = Field(ObjectMetricSource)
    pods = Field(PodsMetricSource)
    resource = Field(ResourceMetricSource)
    type = RequiredField(six.text_type)


class HorizontalPodAutoscalerSpec(Model):
    """
    HorizontalPodAutoscalerSpec describes the desired functionality of the
    HorizontalPodAutoscaler.
    """

    maxReplicas = RequiredField(int)
    metrics = ListField(MetricSpec)
    minReplicas = Field(int)
    scaleTargetRef = RequiredField(CrossVersionObjectReference)


class HorizontalPodAutoscaler(Model):
    """
    HorizontalPodAutoscaler is the configuration for a horizontal pod autoscaler,
    which automatically manages the replica count of any resource implementing the
    scale subresource based on the metrics specified.
    """

    class Meta:
        create_url = "/apis/autoscaling/v2beta2/namespaces/{namespace}/horizontalpodautoscalers"
        delete_url = "/apis/autoscaling/v2beta2/namespaces/{namespace}/horizontalpodautoscalers/{name}"
        get_url = "/apis/autoscaling/v2beta2/namespaces/{namespace}/horizontalpodautoscalers/{name}"
        list_all_url = "/apis/autoscaling/v2beta2/horizontalpodautoscalers"
        list_ns_url = "/apis/autoscaling/v2beta2/namespaces/{namespace}/horizontalpodautoscalers"
        update_url = "/apis/autoscaling/v2beta2/namespaces/{namespace}/horizontalpodautoscalers/{name}"
        watch_url = "/apis/autoscaling/v2beta2/watch/namespaces/{namespace}/horizontalpodautoscalers/{name}"
        watchlist_all_url = "/apis/autoscaling/v2beta2/watch/horizontalpodautoscalers"
        watchlist_ns_url = "/apis/autoscaling/v2beta2/watch/namespaces/{namespace}/horizontalpodautoscalers"

    apiVersion = Field(six.text_type, "autoscaling/v2beta2")
    kind = Field(six.text_type, "HorizontalPodAutoscaler")

    metadata = Field(ObjectMeta)
    spec = Field(HorizontalPodAutoscalerSpec)
    status = Field(HorizontalPodAutoscalerStatus)


class HorizontalPodAutoscalerList(Model):
    """
    HorizontalPodAutoscalerList is a list of horizontal pod autoscaler objects.
    """
    apiVersion = Field(six.text_type, "autoscaling/v2beta2")
    kind = Field(six.text_type, "HorizontalPodAutoscalerList")

    items = ListField(HorizontalPodAutoscaler)
    metadata = Field(ListMeta)