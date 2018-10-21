#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from .post_page import get_user_id_post_page
from .username_checker import username_checker



def likers_protocol(self):
    if len(self.media_by_user) > 0:
        # You have media_id to like:
        self.current_index = random.randint(0, len(self.media_by_user) - 1)
        log_string = "Current Index = %i of %i medias" % (
            self.current_index, len(self.media_by_user))
        self.write_log(log_string)

        likes_count = get_likes_count(self)

        if likes_count >= 10 and likes_count < 100:
            get_user_id_post_page(self, self.media_by_user[self.current_index]["code"])
            username_checker(self)
        del self.media_by_user[self.current_index]


def get_likes_count(self):
    if self.current_index in self.media_by_user:
        if "node" in self.media_by_user[self.current_index]:
            if "edge_liked_by" in self.media_by_user[self.current_index]["node"]:
                if "count" in self.media_by_user[self.current_index]["node"]["edge_liked_by"]:
                    return self.media_by_user[self.current_index]["node"]["edge_liked_by"]["count"]

    return -1;
