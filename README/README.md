# 画像圧縮Webツール（Image Compression Web Tool）

AWSのサーバーレス構成（S3 / Lambda / API Gateway）を用いて作成した、
シンプルな画像圧縮Webサービスです。

AWSの学習を目的として、
「実際に動くWebサービスを構築し、デプロイまで行う」ことをゴールに制作しました。

開発にあたっては AI を補助的に利用しつつ、
アーキテクチャ設計・AWS設定・エラー対応・動作理解は自身で行っています。

---

## 概要

ブラウザから画像をアップロードすると、
AWS Lambda 上で画像を圧縮し、圧縮後の画像を Amazon S3 に保存します。
ユーザーは圧縮済み画像をダウンロードすることができます。

### 主な機能
- 画像のアップロード
- Lambdaによる画像圧縮処理
- 圧縮後画像のS3保存
- 圧縮画像のダウンロード

---

## アーキテクチャ

本サービスは、低コストかつシンプルなサーバーレス構成で実装しています。

ブラウザ（HTML / Vue.js）
↓
API Gateway（REST API）
↓
Lambda（画像圧縮処理）
↓
S3（圧縮画像の保存）


![アーキテクチャ図](architecture/architecture.png)

---

## 使用技術

### フロントエンド
- HTML
- Vue.js
- Bootstrap（v5.3.2）

### バックエンド
- Python 3.11
- Pillow（画像処理ライブラリ）
- AWS SDK（boto3）

### AWS
- Amazon S3（静的サイトホスティング、画像保存）
- AWS Lambda（画像圧縮処理）
- Amazon API Gateway（REST API）
- AWS IAM（権限管理）

---

## ディレクトリ構成

.
├ frontend/
│ └ index.html
├ backend/
│ └ lambda_function.py
├ architecture/
│ └ architecture.png
└ README.md


---

## このツール作成で学んだこと

本プロジェクトを通して、以下のような知識・スキルを身につけました。

- AWSを用いたサーバーレスWebサービスの構築方法
- Lambda依存ライブラリをAmazon Linux環境で準備する必要性
- API Gatewayの設定とCORS対応
- Lambdaの環境変数管理
- CloudWatch Logsを用いたエラー調査・デバッグ
- S3の静的サイトホスティング設定やライフサイクル管理

---

## 今後の改善・拡張案

- Amazon Cognito を用いた認証機能の追加
- Amazon CloudFront による配信高速化
- Amazon SQS を利用した処理の安定化・スケーラビリティ向上
- Terraform / CloudFormation による IaC 化

---

## 関連記事（Qiita）

本プロジェクトの構築手順や学習内容については、
Qiita にてシリーズ記事として公開予定です。

- 第1回：S3の設定と静的サイトホスティング
- 第2回：Lambda関数の実装
- 第3回：API Gatewayの設定と連携

※ 記事公開後にリンクを追記予定

---

## 補足

本リポジトリは学習目的で作成したものです。
本番環境での利用を前提とした最適化やセキュリティ設計は簡略化しています。
