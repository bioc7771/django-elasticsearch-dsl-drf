#!/usr/bin/env bash
cd examples/requirements/
pip-compile base.in "$@"
pip-compile code_style.in "$@"
pip-compile common.in "$@"
pip-compile coreapi_coreschema.in "$@"
pip-compile debug.in "$@"
pip-compile deployment.in "$@"
pip-compile dev.in "$@"
pip-compile django_2_2.in "$@"
pip-compile django_2_2_and_elastic_6x.in "$@"
pip-compile django_2_2_and_elastic_7x.in "$@"
pip-compile django_3_1.in "$@"
pip-compile django_3_1_and_elastic_6x.in "$@"
pip-compile django_3_1_and_elastic_7x.in "$@"
pip-compile django_3_2.in "$@"
pip-compile django_3_2_and_elastic_6x.in "$@"
pip-compile django_3_2_and_elastic_7x.in "$@"
pip-compile docs.in "$@"
pip-compile documentation.in "$@"
pip-compile elastic.in "$@"
pip-compile elastic_6x.in "$@"
pip-compile elastic_7x.in "$@"
pip-compile elastic_docker.in "$@"
pip-compile test.in "$@"
pip-compile testing.in "$@"
