#!/usr/bin/env bash
# SPDX-License-Identifier: MIT
exec 2>&1 gunicorn server:app