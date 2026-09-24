import argparse
from datetime import datetime
import os

parser = argparse.ArgumentParser(description='Logs Analyzer')
parser.add_argument("path", type=str, help="Path to file to analyze")
parser.add_argument("--text", type=str, help="Text to search for", required=True)
args = parser.parse_args()


def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except (PermissionError, UnicodeDecodeError):
        return ""


def split_into_blocks(text):
    blocks = {}
    date_format = "%Y-%m-%d %H:%M:%S.%f"
    date_length = 23
    last_time = None

    for line in text.split('\n'):
        if not line.strip():
            continue
        try:
            block_start = datetime.strptime(line[:date_length], date_format)
            last_time = block_start
            blocks.setdefault(block_start, []).append(line[date_length:].strip())
        except ValueError:
            if last_time is not None:
                blocks[last_time].append(line.strip())

    return blocks


def get_context(block_text, search_text, words=5):
    pos = block_text.find(search_text)
    before = block_text[:pos].split()[-words:]
    after = block_text[pos + len(search_text):].split()[:words]
    return f"...{' '.join(before)} ->{search_text}<- {' '.join(after)}..."


def search_into_blocks(blocks, search_text, file_name):
    results = []
    for time, lines in blocks.items():
        block_text = '\n'.join(lines)
        if search_text in block_text:
            results.append({
                'file': file_name,
                'time': time,
                'context': get_context(block_text, search_text)
            })
    return results


def print_results(results):
    for result in results:
        print(f"Файл: {result['file']}")
        print(f"Время: {result['time']}")
        print(f"Контекст: {result['context']}")
        print("-" * 50)


def main():
    if not os.path.exists(args.path):
        print("Не удалось перейти по указанному пути")
        return

    files_path = []
    if os.path.isfile(args.path):
        files_path.append(args.path)
    else:
        for root, _, filenames in os.walk(args.path):
            for name in filenames:
                files_path.append(os.path.join(root, name))

    final_results = []
    for file in files_path:
        content = read_file(file)
        if not content:
            continue
        blocks = split_into_blocks(content)
        results = search_into_blocks(blocks, args.text, file)
        final_results += results

    print_results(final_results)

    if not final_results:
        print("Текст не найден ни в одном файле")
    else:
        print(f"Всего найдено: {len(final_results)}")


if __name__ == '__main__':
    main()
