# coding: utf-8

from rest_framework import serializers
from .models import User, Post

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'name', 'mail')

class PostSerializer(serializers.ModelSerializer):
  # authorでUserを取得する
  # これはGETのときのみ仕様する
  author = UserSerializer(read_only = True)
  # author_idでPOST時にUserを指定する
  author_id = serializers.PrimaryKeyRelatedField(
    queryset = User.objects.all(),
    source = 'author',
    write_only = True
  )

  class Meta:
    model = Post
    fields = ('title', 'body', 'created_at', 'status', 'author', 'author_id')