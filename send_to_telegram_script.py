stage("Create PDF and Send to Telegram") {
    steps {
        script {
            def pdfFile = sh(script: "python create_pdf_script.py", returnStdout: true).trim()
            sh "python send_to_telegram_script.py $pdfFile $CHAT_ID $TELEGRAM_BOT_TOKEN"
        }
    }
}
