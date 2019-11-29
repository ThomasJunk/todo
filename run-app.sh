#!/usr/bin/env bash
exec 2>&1 gunicorn server:app