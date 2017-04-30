# -*- coding: utf-8 -*-
# Copyright (C) 2014-2017 Andrey Antukh <niwi@niwi.nz>
# Copyright (C) 2014-2017 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014-2017 David Barragán <bameda@dbarragan.com>
# Copyright (C) 2014-2017 Alejandro Alonso <alejandro.alonso@kaleidos.net>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import uuid

from django.core.urlresolvers import reverse

from taiga.base.utils.urls import get_absolute_url


# Set this in settings.PROJECT_MODULES_CONFIGURATORS["github"]
def get_or_generate_config(project):
    config = project.modules_config.config
    if config and "github" in config:
        g_config = project.modules_config.config["github"]
    else:
        g_config = {"secret": uuid.uuid4().hex}

    url = reverse("github-hook-list")
    url = get_absolute_url(url)
    url = "%s?project=%s" % (url, project.id)
    g_config["webhooks_url"] = url

    # Use the default 'TG' project key if not defined
    if not "project_key" in g_config:
        g_config["project_key"] = "TG"

    return g_config
