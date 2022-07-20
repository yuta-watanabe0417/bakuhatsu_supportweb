from watchdog.observers.polling import PollingObserver
from watchdog.events import PatternMatchingEventHandler
from subprocess import run
from pathlib import Path
from re import compile
import time

# 監視対象ディレクトリを指定する
TARGET_DIR = './uploads'
# 監視対象ファイルのパターンマッチを指定する
TARGET_FILE = '*.md'
# FAQファイルパターン
PATTERN_FILE_FAQ = '^FAQ-.+\\.md$'
PATTERN_FILE_INFO = '^INFO-.+\\.md$'


class FileChangeHandler(PatternMatchingEventHandler):
    """
    upload配下のファイルを監視し、イベントを発行します。
    """
    def __init__(self, patterns):
        super(FileChangeHandler, self).__init__(patterns=patterns)

    # 作成イベント
    def on_created(self, event):
        filename = Path(event.src_path).name
        filepath = str(Path(event.src_path))
        if compile(PATTERN_FILE_FAQ).match(filename):
            command_file = 'importFaqMarkdown'
        elif compile(PATTERN_FILE_INFO).match(filename):
            command_file = 'importInformationMarkdown'
        else:
            command_file = 'importContentsMarkdown'
        run(["python", "manage.py", command_file, "-a", "created", "-f" + filepath])

    # 更新イベント
    def on_modified(self, event):
        filename = Path(event.src_path).name
        filepath = str(Path(event.src_path))
        print('%s modified' % filepath)
        if compile(PATTERN_FILE_FAQ).match(filename):
            command_file = 'importFaqMarkdown'
        elif compile(PATTERN_FILE_INFO).match(filename):
            command_file = 'importInformationMarkdown'
        else:
            command_file = 'importContentsMarkdown'
        run(["python", "manage.py", command_file, "-a", "modified", "-f" + filepath])

    # 削除イベント
    def on_deleted(self, event):
        filename = Path(event.src_path).name
        filepath = str(Path(event.src_path))
        print('%s deleted' % filepath)
        if compile(PATTERN_FILE_FAQ).match(filename):
            command_file = 'importFaqMarkdown'
        elif compile(PATTERN_FILE_INFO).match(filename):
            command_file = 'importInformationMarkdown'
        else:
            command_file = 'importContentsMarkdown'
        run(["python", "manage.py", command_file, "-a", "deleted", "-f" + filepath])


# コマンド実行の確認
if __name__ == "__main__":
    # ファイル監視の開始
    observer = PollingObserver()
    observer.schedule(FileChangeHandler([TARGET_FILE]), TARGET_DIR, recursive=True)
    observer.start()

    # 処理が終了しないようスリープを挟んで無限ループ
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
