# =====================================================
# INTRODUCTION TO APIs
# =====================================================

# API = Application Programming Interface

# An API allows two applications to communicate
# with each other by sending requests and responses.

# Example:
#
# Mobile App
#      │
#      ▼
# REST API
#      │
#      ▼
# Django Application
#      │
#      ▼
# Database

# Examples of APIs:
#
# Weather API
# Google Maps API
# Payment API
# Chat API

# Django provides APIs using
# Django REST Framework (DRF).


# =====================================================
# REST (Representational State Transfer)
# =====================================================

# REST is an architectural style used to build APIs.

# REST APIs communicate using HTTP methods.

# Common HTTP Methods

# GET
# Retrieve data

# POST
# Create data

# PUT
# Update complete data

# PATCH
# Update partial data

# DELETE
# Delete data



# =====================================================
# REST PRINCIPLES
# =====================================================

# 1. Client-Server Architecture
#
# Client and server are independent.

# 2. Stateless
#
# Every request contains all required information.
# The server does not remember previous requests.

# 3. Uniform Interface
#
# Standard URLs and HTTP methods.

# 4. Resource-Based
#
# Everything is treated as a resource.
#
# Example:
#
# /students/
# /courses/
# /employees/

# 5. Cacheable
#
# Responses may be cached to improve performance.

# 6. Layered System
#
# Requests may pass through proxies,
# gateways, or load balancers.


# =====================================================
# COMMON HTTP STATUS CODES
# =====================================================

# 200 OK
# Request successful

# 201 Created
# Resource created successfully

# 204 No Content
# Resource deleted successfully

# 400 Bad Request
# Invalid request

# 401 Unauthorized
# Authentication required

# 403 Forbidden
# Permission denied

# 404 Not Found
# Resource not found

# 500 Internal Server Error
# Server error



# =====================================================
# SERIALIZERS
# =====================================================

# A Serializer converts Django Model objects
# into JSON format and converts JSON data
# back into Python objects.

# Similar to Django ModelForm,
# but used for REST APIs.

# Serialization
#
# Model Object
#      │
#      ▼
# Serializer
#      │
#      ▼
# JSON

# Deserialization
#
# JSON
#      │
#      ▼
# Serializer
#      │
#      ▼
# Model Object



# =====================================================
# API VIEWS
# =====================================================

# APIView is the base class for
# creating REST APIs in Django REST Framework.

# It supports:
#
# GET
# POST
# PUT
# PATCH
# DELETE