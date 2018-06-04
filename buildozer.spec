[app]

title = Tursan

package.name = tursan

package.domain = herotek.ir

source.dir = .

source.include_exts = py,png,jpg,kv,atlas

version.regex= __version__ = '(.*)'
version.filename = %(source.dir)s/main.py

requiremets = kivy


presplash.filename = %(source.dir)s/pre.jpg

icon.filename = %(source.dir)s/icon.png

fullscreen = 1

android.api = 19
android.minapi = 13

android.sdk = 23


[buildozer]

log_level = 2