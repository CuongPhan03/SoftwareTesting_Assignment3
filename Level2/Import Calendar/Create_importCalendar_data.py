import json

# Tạo dữ liệu dạng list
url_data = [
    {"name": "", "url": "", "expected": "- Required"},
    {"name": "a", "url": "", "expected": "Either a URL or a file is required to import a calendar."},
    {"name": "", "url": "a", "expected": "- Required"},
    {"name": "a", "url": "a", "expected": "The given iCal URL is invalid."},
    {"name": "", "url": "https://vn.search.yahoo.com/search?fr=mcafee&type=E210VN91215G0&p=calendar", "expected": "- Required"},
    {"name": "a", "url": "https://vn.search.yahoo.com/search?fr=mcafee&type=E210VN91215G0&p=calendar", "expected": "The given iCal URL is invalid."},
    {"name": "", "url": "https://calendar.google.com/calendar/u/0/r", "expected": "- Required"},
    {"name": "a", "url": "https://calendar.google.com/calendar/u/0/r", "expected": "Import or export calendars"}
]
file_data = [
        {
            "name": "",
            "file": "",
            "expected": "- Required"
        },
        {
            "name": "a",
            "file": "",
            "expected": "Either a URL or a file is required to import a calendar."
        },
        {
            "name": "",
            "file": "C:\\\\Test\\\\test.txt",
            "expected": "Text file filetype cannot be accepted."
        },
        {
            "name": "a",
            "file": "C:\\\\Test\\\\test.txt",
            "expected": "Text file filetype cannot be accepted."
        },
        {
            "name": "",
            "file": "C:\\\\Test\\\\event.ics",
            "expected": "The file 'event.ics' is either empty or a folder. To upload folders zip them first."
        },
        {
            "name": "a",
            "file": "C:\\\\Test\\\\event.ics",
            "expected": "The file 'event.ics' is either empty or a folder. To upload folders zip them first."
        },
        {
            "name": "",
            "file": "C:\\\\Test\\\\event_1.ics",
            "expected": "- Required"
        },
        {
            "name": "a",
            "file": "C:\\\\Test\\\\event_1.ics",
            "expected": "Import or export calendars"
        },
        {
            "name": "",
            "file": "C:\\\\Test\\\\test_1.txt",
            "expected": "The file 'test_1.txt' is either empty or a folder. To upload folders zip them first."
        },
        {
            "name": "a",
            "file": "C:\\\\Test\\\\test_1.txt",
            "expected": "The file 'test_1.txt' is either empty or a folder. To upload folders zip them first."
        }
]
authen = [
    {"username": "manager", "password": "sandbox24"}
]

# Kết hợp dữ liệu
combined_url_data = {
    "url_data": url_data,
    "authen": authen
}
combined_file_data = {
    "file_data": file_data,
    "authen": authen
}

# Ghi dữ liệu vào file JSON
with open('Input_calendar_url_test.json', 'w', encoding='utf-8') as file:
    json.dump(combined_url_data, file, indent=4, ensure_ascii=False)
with open('Input_calendar_file_test.json', 'w', encoding='utf-8') as file:
    json.dump(combined_file_data, file, indent=4, ensure_ascii=False)
print("File JSON đã được ghi thành công!")