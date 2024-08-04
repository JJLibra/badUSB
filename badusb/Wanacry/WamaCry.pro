QT += core gui
QT += multimedia

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = WamaCry
TEMPLATE = app

DEFINES += QT_DEPRECATED_WARNINGS

SOURCES += main.cpp\
        wamacry.cpp

HEADERS  += wamacry.h

FORMS    += wamacry.ui

RC_ICONS =ico.ico

# 添加 QAESEncryption 库
INCLUDEPATH += $$PWD/libs/qaesencryption
SOURCES += $$PWD/libs/qaesencryption/qaesencryption.cpp
HEADERS += $$PWD/libs/qaesencryption/qaesencryption.h
