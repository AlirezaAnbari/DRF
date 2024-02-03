{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ name }}
{% endblock %}

{% block html %}

This is an <strong>html</strong> message for checking email with mail-templated module.
<img src="https://img.etimg.com/thumb/msid-89705853,width-650,height-488,imgsize-44124,resizemode-75/crypto.jpg">

{% endblock %}