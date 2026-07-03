# pip install reportlab nếu tải file pdf mà không phải text
import random
import hashlib
import sys
import os
import re

#

### EDIT HERE
FILE_COUNT = 10  # số file
PAGES = None  # None = random 5-10
OUTPUT_FORMAT = "pdf"  # "pdf" hoặc "txt"
OUTPUT_NAME = None  # ví dụ: "report.pdf"
OUTPUT_DIR = "output"  # thư mục lưu file
### END OF EDIT

CONSONANTS = list("bcdfghjklmnprstvwxz")
VOWELS = list("aeiou")
CLUSTERS = [
    "tr",
    "bl",
    "fr",
    "gr",
    "cl",
    "fl",
    "pr",
    "st",
    "sp",
    "sk",
    "dr",
    "br",
    "cr",
    "gl",
    "sl",
    "sm",
    "sn",
    "sw",
    "th",
    "wh",
]
ENDINGS = ["", "n", "m", "t", "s", "k", "l", "r", "nd", "st", "nt", "ng", "ld", "lt"]

CONNECTORS = [
    # Tiếng Việt
    "và",
    "nhưng",
    "tuy nhiên",
    "do đó",
    "vì vậy",
    "mặc dù",
    "hơn nữa",
    "bên cạnh đó",
    "trong khi đó",
    "đồng thời",
    "theo đó",
    "ngoài ra",
    "cụ thể là",
    "nói chung",
    "thực ra",
    "mặt khác",
    "dù sao",
    "đặc biệt",
    "chẳng hạn",
    "ví dụ",
    "tóm lại",
    "kết quả là",
    "cuối cùng",
    "đầu tiên",
    "thứ hai",
    "tiếp theo",
    "sau đó",
    "trước hết",
    "ngược lại",
    "trái lại",
    "vì thế",
    "do vậy",
    "thế nên",
    "nhờ đó",
    "bởi vậy",
    "bởi thế",
    "bởi vì",
    "vì",
    "nếu vậy",
    "nếu không",
    "thậm chí",
    "không những thế",
    "hơn thế nữa",
    "không chỉ vậy",
    "một mặt",
    "mặt khác",
    "trên thực tế",
    "thật vậy",
    "rõ ràng",
    "dẫu vậy",
    "tựu trung",
    "xét cho cùng",
    "điều này có nghĩa là",
    "nói cách khác",
    "hay nói cách khác",
    "đồng nghĩa với việc",
    "đáng chú ý",
    "điển hình là",
    "nhìn chung",
    "tổng thể",
    "về cơ bản",
    "theo quan điểm đó",
    "từ đó",
    "qua đó",
    "đi kèm với",
    "song song đó",
    "không chỉ thế",
    "thêm vào đó",
    "đặc biệt hơn",
    "nói tóm lại",
    "xét về tổng thể",
    "dẫu thế",
    "ngay cả khi",
    "miễn là",
    "trong trường hợp đó",
    "kế đến",
    "cuối cùng thì",
    "nhân tiện",
    "cũng vì thế",
    "therefore",
    "however",
    "furthermore",
    "meanwhile",
    "consequently",
    "in addition",
    "on the other hand",
    "as a result",
    "for instance",
    "for example",
    "moreover",
    "thus",
    "hence",
    "nevertheless",
    "nonetheless",
    "instead",
    "otherwise",
    "similarly",
    "likewise",
    "in contrast",
    "by contrast",
    "in fact",
    "indeed",
    "overall",
    "finally",
    "first",
    "second",
    "next",
    "then",
    "afterward",
    "beforehand",
    "at the same time",
    "in the meantime",
    "in conclusion",
    "to summarize",
    "in short",
    "ultimately",
    "accordingly",
]

FILLER_PHRASES = [
    "trong bối cảnh đó",
    "xét về mặt tổng thể",
    "theo quan điểm này",
    "dựa trên các yếu tố trên",
    "về cơ bản mà nói",
    "một cách khách quan",
    "nhìn từ góc độ khác",
    "tại thời điểm hiện tại",
    "từ góc nhìn đa chiều",
    "trong phạm vi nghiên cứu",
    "ở một khía cạnh khác",
    "xét trên nhiều phương diện",
    "điều đáng chú ý là",
    "không thể phủ nhận rằng",
    "cần phải nhấn mạnh rằng",
    "điều này cho thấy",
    "thực tế cho thấy",
    "có thể nhận thấy rằng",
    "có thể thấy rõ rằng",
    "đáng lưu ý là",
    "trên thực tế",
    "một điều quan trọng là",
    "ở góc độ thực tiễn",
    "trong trường hợp này",
    "từ thực tế hiện nay",
    "về lâu dài",
    "về ngắn hạn",
    "ở mức độ nhất định",
    "xét theo tình hình hiện nay",
    "ở khía cạnh này",
    "ở phương diện khác",
    "xét về bản chất",
    "về mặt lý thuyết",
    "về mặt thực tiễn",
    "trong điều kiện hiện nay",
    "theo cách tiếp cận này",
    "ở góc nhìn tổng quát",
    "trong nhiều trường hợp",
    "trong hầu hết các trường hợp",
    "xét một cách toàn diện",
    "nhìn chung mà nói",
    "có thể hiểu rằng",
    "có thể khẳng định rằng",
    "điều cần lưu ý là",
    "không khó để nhận thấy",
    "ở mức độ tổng quan",
    "trên phương diện này",
    "ở khía cạnh tổng thể",
    "về tổng thể",
    "xét một cách khách quan",
    "trong hoàn cảnh hiện tại",
    "theo xu hướng chung",
    "trong thực tế",
    "trên cơ sở đó",
    "từ những phân tích trên",
    "từ những dữ liệu hiện có",
    "dựa trên thực tế",
    "căn cứ vào đó",
    "từ góc nhìn thực tiễn",
    "ở phạm vi rộng hơn",
    "ở phạm vi hẹp hơn",
    "trên bình diện chung",
    "về mặt chiến lược",
    "về mặt vận hành",
    "từ quan điểm cá nhân",
    "theo đánh giá chung",
    "nhìn một cách tổng quan",
    "điều này đồng nghĩa với việc",
    "xét cho cùng",
    "suy cho cùng",
    "ở thời điểm này",
    "tính đến hiện tại",
    "ở cấp độ tổng thể",
    "ở cấp độ chi tiết",
    "từ khía cạnh kỹ thuật",
    "từ khía cạnh kinh tế",
    "từ khía cạnh xã hội",
    "ở góc nhìn học thuật",
    "ở góc nhìn thực tế",
    "theo hướng tiếp cận hiện đại",
    "ở một mức độ nào đó",
    "không nằm ngoài xu hướng chung",
    "có thể lý giải rằng",
    "đây là một yếu tố quan trọng",
    "điều này phản ánh rằng",
    "cần được xem xét kỹ hơn",
    "đây là cơ sở để",
    "trong bức tranh tổng thể",
    "ở khía cạnh dài hạn",
    "ở khía cạnh ngắn hạn",
    "trong nhiều tình huống",
    "theo kinh nghiệm thực tế",
    "xét trên bình diện rộng",
    "ở góc độ quản lý",
    "ở góc độ người dùng",
    "xét theo bối cảnh hiện nay",
    "với cách nhìn toàn diện",
    "theo các phân tích gần đây",
    "dựa trên các bằng chứng hiện có",
    "từ đó có thể thấy rằng",
    "nhìn một cách khách quan",
]

SECTION_TITLES = [
    "Phần {n}: Khảo sát ban đầu",
    "Chương {n}: Phân tích dữ liệu",
    "Mục {n}: Đánh giá kết quả",
    "Phần {n}: Tổng hợp thông tin",
    "Chương {n}: Nhận định chuyên sâu",
    "Mục {n}: Triển khai mô hình",
    "Phần {n}: Kết luận trung gian",
    "Chương {n}: Xem xét các trường hợp",
    "Mục {n}: So sánh và đối chiếu",
    "Phần {n}: Nghiên cứu bổ sung",
    "Chương {n}: Giới thiệu",
    "Phần {n}: Tổng quan",
    "Mục {n}: Cơ sở lý thuyết",
    "Chương {n}: Phương pháp nghiên cứu",
    "Phần {n}: Thiết kế hệ thống",
    "Mục {n}: Kiến trúc tổng thể",
    "Chương {n}: Thu thập dữ liệu",
    "Phần {n}: Tiền xử lý dữ liệu",
    "Mục {n}: Chuẩn hóa dữ liệu",
    "Chương {n}: Làm sạch dữ liệu",
    "Phần {n}: Mô hình hóa",
    "Mục {n}: Thiết lập tham số",
    "Chương {n}: Kiểm thử",
    "Phần {n}: Kiểm định",
    "Mục {n}: Đánh giá hiệu năng",
    "Chương {n}: Phân tích thống kê",
    "Phần {n}: Trực quan hóa dữ liệu",
    "Mục {n}: Kết quả thực nghiệm",
    "Chương {n}: Thảo luận",
    "Phần {n}: Kết luận",
    "Mục {n}: Đề xuất cải tiến",
    "Chương {n}: Hướng phát triển",
    "Phần {n}: Tài liệu tham khảo",
    "Mục {n}: Phụ lục",
    "Chương {n}: Mô tả bài toán",
    "Phần {n}: Phân tích yêu cầu",
    "Mục {n}: Đặc tả chức năng",
    "Chương {n}: Thiết kế giao diện",
    "Phần {n}: Thiết kế cơ sở dữ liệu",
    "Mục {n}: Luồng xử lý",
    "Chương {n}: Thiết kế API",
    "Phần {n}: Bảo mật hệ thống",
    "Mục {n}: Kiểm soát truy cập",
    "Chương {n}: Tối ưu hiệu suất",
    "Phần {n}: Quản lý tài nguyên",
    "Mục {n}: Khả năng mở rộng",
    "Chương {n}: Giải pháp triển khai",
    "Phần {n}: Cấu hình môi trường",
    "Mục {n}: Giám sát hệ thống",
    "Chương {n}: Phân tích log",
    "Phần {n}: Xử lý ngoại lệ",
    "Mục {n}: Kiểm thử bảo mật",
    "Chương {n}: Kiểm thử tải",
    "Phần {n}: Kiểm thử tích hợp",
    "Mục {n}: Kiểm thử người dùng",
    "Chương {n}: Phân tích rủi ro",
    "Phần {n}: Đánh giá chi phí",
    "Mục {n}: Phân tích lợi ích",
    "Chương {n}: So sánh giải pháp",
    "Phần {n}: Đánh giá tổng thể",
    "Mục {n}: Phân tích thuật toán",
    "Chương {n}: Tối ưu thuật toán",
    "Phần {n}: Phân tích độ phức tạp",
    "Mục {n}: So sánh mô hình",
    "Chương {n}: Thử nghiệm thực tế",
    "Phần {n}: Đánh giá người dùng",
    "Mục {n}: Thu thập phản hồi",
    "Chương {n}: Phân tích xu hướng",
    "Phần {n}: Đánh giá tác động",
    "Mục {n}: Khả năng ứng dụng",
    "Chương {n}: Định hướng phát triển",
    "Phần {n}: Giải pháp thay thế",
    "Mục {n}: Các giả định",
    "Chương {n}: Giới hạn nghiên cứu",
    "Phần {n}: Các vấn đề tồn tại",
    "Mục {n}: Hướng khắc phục",
    "Chương {n}: Tổng hợp kết quả",
    "Phần {n}: Phân tích chi tiết",
    "Mục {n}: Kết quả định lượng",
    "Chương {n}: Kết quả định tính",
    "Phần {n}: Đánh giá thực tiễn",
    "Mục {n}: Phân tích trường hợp",
    "Chương {n}: Khảo sát thị trường",
    "Phần {n}: Đánh giá công nghệ",
    "Mục {n}: Phân tích kiến trúc",
    "Chương {n}: Thiết kế giải pháp",
    "Phần {n}: Mô phỏng hệ thống",
    "Mục {n}: Thực nghiệm mở rộng",
    "Chương {n}: Phân tích hiệu quả",
    "Phần {n}: Tổng kết",
    "Mục {n}: Kiến nghị",
    "Chương {n}: Kế hoạch triển khai",
    "Phần {n}: Định hướng tương lai",
    "Mục {n}: Bài học kinh nghiệm",
    "Chương {n}: Quy trình thực hiện",
    "Phần {n}: Kiểm chứng mô hình",
    "Mục {n}: Xác minh kết quả",
    "Chương {n}: Kết luận cuối cùng",
    "Phần {n}: Tóm tắt nội dung",
    "Mục {n}: Ghi chú bổ sung",
]

DOCUMENT_TITLES = [
    "Báo Cáo Phân Tích Hiệu Suất Hệ Thống Quản Lý Kho",
    "Tổng Hợp Kiến Thức Cơ Bản Về Mạng Máy Tính",
    "Nghiên Cứu Ứng Dụng AI Trong Nhận Diện Hình Ảnh",
    "Tài Liệu Hướng Dẫn Thiết Kế Cơ Sở Dữ Liệu Oracle",
    "Báo Cáo Đánh Giá Chất Lượng Dịch Vụ Logistics",
    "Phân Tích Thuật Toán Tối Ưu Đường Đi Ngắn Nhất",
    "Đề Tài Nghiên Cứu Hành Vi Người Dùng Trên Website",
    "Chuyên Đề An Toàn Thông Tin Trong Doanh Nghiệp",
    "Báo Cáo Thực Tập Hệ Thống Quản Lý Nhân Sự",
    "Tổng Quan Công Nghệ Điện Toán Đám Mây",
    "Phân Tích Dữ Liệu Doanh Thu Quý II Năm 2025",
    "Tài Liệu Kiểm Thử Phần Mềm Và Quy Trình QA",
    "Báo Cáo Khảo Sát Hiệu Năng API Nội Bộ",
    "Nghiên Cứu Giải Pháp Tự Động Hóa Quy Trình Sản Xuất",
    "Đồ Án Thiết Kế Ứng Dụng Quản Lý Công Việc",
    "Chuyên Đề Xử Lý Ảnh Và Nhận Dạng Ký Tự OCR",
    "Báo Cáo Phân Tích Tải Trọng Máy Chủ Linux",
    "Tài Liệu Học Tập Lập Trình Python Nâng Cao",
    "Nghiên Cứu So Sánh MongoDB Và PostgreSQL",
    "Báo Cáo Kiểm Tra Tính Ổn Định Của Hệ Thống RFID",
    "Tổng Quan Về Trí Tuệ Nhân Tạo Tạo Sinh",
    "Báo Cáo Phân Tích Dữ Liệu Bán Hàng",
    "Nghiên Cứu Hệ Thống Khuyến Nghị Sản Phẩm",
    "Thiết Kế Kiến Trúc Microservices",
    "Tài Liệu Triển Khai Kubernetes",
    "Báo Cáo Đánh Giá Hiệu Quả SEO",
    "Hướng Dẫn Xây Dựng RESTful API",
    "Phân Tích Hiệu Năng Cơ Sở Dữ Liệu",
    "Đề Tài Khai Phá Dữ Liệu",
    "Tài Liệu DevOps Cho Doanh Nghiệp",
    "Báo Cáo Kiểm Thử Bảo Mật Web",
    "Phân Tích Nhật Ký Hệ Thống",
    "Nghiên Cứu Blockchain Trong Tài Chính",
    "Báo Cáo Đánh Giá Rủi Ro CNTT",
    "Đồ Án Hệ Thống Quản Lý Thư Viện",
    "Tài Liệu Thiết Kế UX/UI",
    "Báo Cáo Khảo Sát Người Dùng",
    "Nghiên Cứu Deep Learning",
    "Ứng Dụng Machine Learning Trong Y Tế",
    "Hướng Dẫn Docker Cho Người Mới",
    "Báo Cáo Giám Sát Hệ Thống",
    "Tổng Quan Về Data Warehouse",
    "Thiết Kế Kiến Trúc Data Lake",
    "Báo Cáo Phân Tích Big Data",
    "Nghiên Cứu Học Tăng Cường",
    "Chuyên Đề NLP Tiếng Việt",
    "Báo Cáo Hiệu Suất Redis",
    "Tài Liệu RabbitMQ Và Kafka",
    "Nghiên Cứu Apache Spark",
    "Phân Tích Elasticsearch",
    "Hướng Dẫn Git Và GitHub",
    "Tài Liệu CI/CD Jenkins",
    "Đánh Giá Azure Cloud",
    "Đánh Giá AWS Cloud",
    "Đánh Giá Google Cloud Platform",
    "Phân Tích Chi Phí Hạ Tầng Cloud",
    "Tài Liệu Terraform",
    "Báo Cáo Kubernetes Cluster",
    "Tổng Quan Về IoT",
    "Ứng Dụng IoT Trong Nông Nghiệp",
    "Nghiên Cứu Mạng 5G",
    "Phân Tích Giao Thức MQTT",
    "Báo Cáo Hệ Thống Camera AI",
    "Đồ Án Smart Home",
    "Tài Liệu Embedded Linux",
    "Báo Cáo Điều Khiển Robot",
    "Nghiên Cứu Xe Tự Hành",
    "Phân Tích Thuật Toán SLAM",
    "Hướng Dẫn OpenCV",
    "Ứng Dụng YOLO Trong Nhận Diện Đối Tượng",
    "Báo Cáo OCR Tiếng Việt",
    "Phân Tích Nhận Dạng Khuôn Mặt",
    "Nghiên Cứu Voice Recognition",
    "Báo Cáo Chatbot AI",
    "Thiết Kế Hệ Thống CRM",
    "Thiết Kế Hệ Thống ERP",
    "Đánh Giá Hệ Thống POS",
    "Phân Tích Chuỗi Cung Ứng",
    "Báo Cáo Quản Lý Dự Án Agile",
    "Tài Liệu Scrum Framework",
    "Hướng Dẫn Kanban",
    "Nghiên Cứu Quản Lý Rủi Ro",
    "Đánh Giá KPI Doanh Nghiệp",
    "Phân Tích Hiệu Quả Marketing",
    "Báo Cáo Google Analytics",
    "Nghiên Cứu Hành Vi Khách Hàng",
    "Phân Tích Chuyển Đổi Bán Hàng",
    "Báo Cáo Tối Ưu Website",
    "Tài Liệu ReactJS Nâng Cao",
    "Tài Liệu VueJS Thực Hành",
    "Hướng Dẫn Angular",
    "Đồ Án Node.js",
    "Đồ Án Django",
    "Đồ Án Laravel",
    "Phân Tích Java Spring Boot",
    "Tài Liệu ASP.NET Core",
    "Nghiên Cứu Flutter",
    "Đồ Án Android",
    "Đồ Án iOS Swift",
    "Báo Cáo Phân Tích Nhật Ký Truy Cập",
    "Tài Liệu Thiết Kế API Gateway",
    "Nghiên Cứu Zero Trust Security",
    "Báo Cáo Quản Trị Hệ Thống Windows Server",
]

_generated_words: set[str] = set()


def make_syllable() -> str:
    style = random.randint(0, 3)
    if style == 0:
        return (
            random.choice(CONSONANTS) + random.choice(VOWELS) + random.choice(ENDINGS)
        )
    elif style == 1:
        return random.choice(CLUSTERS) + random.choice(VOWELS) + random.choice(ENDINGS)
    elif style == 2:
        return (
            random.choice(VOWELS) + random.choice(CONSONANTS) + random.choice(ENDINGS)
        )
    else:
        return random.choice(CONSONANTS) + random.choice(VOWELS) + random.choice(VOWELS)


def make_word(min_syllables: int = 1, max_syllables: int = 3) -> str:
    for _ in range(200):
        n = random.randint(min_syllables, max_syllables)
        word = "".join(make_syllable() for _ in range(n))
        if word not in _generated_words:
            _generated_words.add(word)
            return word
    base = "".join(make_syllable() for _ in range(2))
    suffix = hashlib.md5(base.encode()).hexdigest()[:4]
    unique = base + suffix
    _generated_words.add(unique)
    return unique


def make_sentence(word_count_range=(8, 20)) -> str:
    n_words = random.randint(*word_count_range)
    words = []
    for i in range(n_words):
        if i > 0 and random.random() < 0.08:
            words.append(random.choice(CONNECTORS))
        if i > 0 and random.random() < 0.05:
            words.append(random.choice(FILLER_PHRASES))
            continue
        syl = random.choices([1, 2, 3], weights=[3, 5, 2])[0]
        words.append(make_word(syl, syl))
    sentence = " ".join(words)
    sentence = sentence[0].upper() + sentence[1:]
    ending = random.choices([".", ".", ".", "!", "?"], weights=[7, 7, 7, 2, 2])[0]
    return sentence + ending


def make_paragraph(sentence_count_range=(4, 8)) -> str:
    n = random.randint(*sentence_count_range)
    return " ".join(make_sentence() for _ in range(n))


TABLE_COLUMN_HEADERS = [
    ["STT", "Mã", "Tên", "Giá trị", "Ghi chú"],
    ["ID", "Thời gian", "Người thực hiện", "Kết quả", "Trạng thái"],
    ["Mã số", "Hạng mục", "Số lượng", "Đơn giá", "Thành tiền"],
    ["STT", "Chỉ tiêu", "Đơn vị", "Giá trị", "Tỷ lệ %"],
    ["Mã", "Tên đối tượng", "Ngày bắt đầu", "Ngày kết thúc", "Tiến độ"],
    ["STT", "Nhóm", "Phân loại", "Mô tả", "Đánh giá"],
    ["ID", "Tên", "Email", "Vai trò", "Trạng thái"],
    ["STT", "Sản phẩm", "Danh mục", "Giá", "Kho"],
    ["STT", "Khách hàng", "Địa chỉ", "Điện thoại", "Ghi chú"],
    ["Mã NV", "Họ tên", "Phòng ban", "Chức vụ", "Lương"],
    ["Mã SV", "Họ tên", "Lớp", "Điểm", "Xếp loại"],
    ["Mã MH", "Tên môn", "Số tín chỉ", "Giảng viên", "Học kỳ"],
    ["STT", "Thiết bị", "Model", "Serial", "Tình trạng"],
    ["Mã", "Dự án", "Quản lý", "Ngân sách", "Tiến độ"],
    ["STT", "Công việc", "Người phụ trách", "Hạn chót", "Trạng thái"],
    ["ID", "API", "Endpoint", "Method", "Mô tả"],
    ["Mã", "Module", "Phiên bản", "Ngày cập nhật", "Ghi chú"],
    ["STT", "Server", "CPU", "RAM", "Disk"],
    ["Tên máy", "IP", "Hệ điều hành", "Uptime", "Trạng thái"],
    ["ID", "Container", "Image", "Status", "Port"],
    ["STT", "Log ID", "Timestamp", "Level", "Message"],
    ["ID", "Người dùng", "Hành động", "Thời gian", "IP"],
    ["STT", "URL", "Method", "Status Code", "Latency"],
    ["Mã", "Tên file", "Dung lượng", "Định dạng", "Ngày tạo"],
    ["STT", "Thư mục", "Số file", "Dung lượng", "Chủ sở hữu"],
    ["ID", "Database", "Table", "Rows", "Size"],
    ["Mã", "Query", "Execution Time", "Rows", "Status"],
    ["STT", "Service", "CPU %", "RAM %", "Health"],
    ["ID", "Process", "PID", "Memory", "CPU %"],
    ["Mã", "Job", "Schedule", "Last Run", "Result"],
    ["STT", "Thuật toán", "Độ chính xác", "Recall", "F1-Score"],
    ["ID", "Dataset", "Số mẫu", "Train", "Test"],
    ["Epoch", "Loss", "Accuracy", "Validation", "Learning Rate"],
    ["Mô hình", "Precision", "Recall", "F1", "AUC"],
    ["STT", "Feature", "Kiểu dữ liệu", "Ý nghĩa", "Nguồn"],
    ["ID", "Biến", "Min", "Max", "Mean"],
    ["STT", "Thuộc tính", "Giá trị", "Đơn vị", "Mô tả"],
    ["ID", "Tham số", "Giá trị", "Mặc định", "Ghi chú"],
    ["Mã", "Experiment", "Seed", "Score", "Kết quả"],
    ["STT", "Mô hình", "Framework", "Version", "Hiệu suất"],
    ["ID", "Sự cố", "Mức độ", "Người xử lý", "Trạng thái"],
    ["STT", "Lỗi", "Mô tả", "Độ ưu tiên", "Kết quả"],
    ["Bug ID", "Module", "Severity", "Assignee", "Status"],
    ["Ticket", "Người tạo", "Ngày tạo", "Deadline", "Trạng thái"],
    ["Case", "Input", "Expected", "Actual", "Pass/Fail"],
    ["STT", "Test Case", "Kết quả", "Tester", "Ngày kiểm thử"],
    ["ID", "Build", "Version", "Ngày phát hành", "Trạng thái"],
    ["Release", "Feature", "Owner", "ETA", "Status"],
    ["Issue", "Component", "Priority", "Resolution", "Comment"],
    ["ID", "Change", "Author", "Review", "Merge"],
    ["STT", "Doanh thu", "Chi phí", "Lợi nhuận", "Tăng trưởng"],
    ["Tháng", "Doanh thu", "Chi phí", "ROI", "Ghi chú"],
    ["Quý", "Doanh số", "Khách hàng", "Đơn hàng", "Tỷ lệ"],
    ["Năm", "Doanh thu", "Lợi nhuận", "Thuế", "Tổng cộng"],
    ["STT", "Khoản mục", "Ngân sách", "Thực tế", "Chênh lệch"],
    ["ID", "Đơn hàng", "Khách hàng", "Giá trị", "Thanh toán"],
    ["Mã HĐ", "Ngày", "Khách hàng", "Tổng tiền", "Trạng thái"],
    ["STT", "Sản phẩm", "SL bán", "Doanh thu", "Lợi nhuận"],
    ["Mã", "Nhà cung cấp", "Giá", "VAT", "Ghi chú"],
    ["STT", "Chi nhánh", "Doanh số", "Nhân viên", "Đánh giá"],
    ["ID", "Thành phố", "Dân số", "Diện tích", "Ghi chú"],
    ["STT", "Quốc gia", "Thủ đô", "Dân số", "GDP"],
    ["Mã", "Khu vực", "Nhiệt độ", "Độ ẩm", "Áp suất"],
    ["Ngày", "Nhiệt độ", "Lượng mưa", "Gió", "Thời tiết"],
    ["STT", "Địa điểm", "Kinh độ", "Vĩ độ", "Độ cao"],
    ["ID", "Cảm biến", "Giá trị", "Đơn vị", "Timestamp"],
    ["STT", "Loại dữ liệu", "Nguồn", "Tần suất", "Mức tin cậy"],
    ["ID", "Đối tượng", "Thuộc tính", "Giá trị", "Mô tả"],
    ["STT", "Danh mục", "Số lượng", "Tỷ trọng", "Ghi chú"],
    ["Mã", "Loại", "Phiên bản", "Ngày phát hành", "Trạng thái"],
    ["ID", "Username", "Role", "Last Login", "Status"],
    ["STT", "Repository", "Branch", "Commit", "Author"],
    ["ID", "Pull Request", "Reviewer", "Merge", "Status"],
    ["STT", "Workflow", "Trigger", "Duration", "Result"],
    ["ID", "Pipeline", "Stage", "Time", "Status"],
    ["Mã", "Backup", "Dung lượng", "Ngày", "Kết quả"],
    ["STT", "Snapshot", "Machine", "Size", "Created"],
    ["ID", "Cluster", "Node", "Pods", "Health"],
    ["STT", "Namespace", "Deployment", "Replicas", "Ready"],
    ["ID", "Secret", "Type", "Namespace", "Updated"],
    ["STT", "Email", "Người gửi", "Tiêu đề", "Ngày gửi"],
    ["ID", "Tài liệu", "Tác giả", "Phiên bản", "Ngày sửa"],
    ["STT", "Bài viết", "Chuyên mục", "Lượt xem", "Đánh giá"],
    ["ID", "Video", "Thời lượng", "Định dạng", "Kích thước"],
    ["STT", "Hình ảnh", "Độ phân giải", "Dung lượng", "Định dạng"],
    ["ID", "Âm thanh", "Bitrate", "Thời lượng", "Codec"],
    ["STT", "File", "Checksum", "Hash", "Trạng thái"],
    ["ID", "Tác vụ", "Ưu tiên", "Người xử lý", "Deadline"],
    ["STT", "Phiên họp", "Người tham dự", "Thời gian", "Kết luận"],
    ["ID", "Biểu mẫu", "Người tạo", "Ngày tạo", "Trạng thái"],
]


def make_table() -> dict:
    """Sinh bảng ngẫu nhiên: {'headers': [str], 'rows': [[str]]}"""
    headers = random.choice(TABLE_COLUMN_HEADERS)
    n_cols = len(headers)
    n_rows = random.randint(3, 7)
    rows = []
    for i in range(n_rows):
        row = []
        for j in range(n_cols):
            if j == 0:
                row.append(str(i + 1))
            elif j == n_cols - 1:
                val = random.random()
                if val < 0.3:
                    row.append("Hoàn thành")
                elif val < 0.5:
                    row.append("Đang xử lý")
                elif val < 0.7:
                    row.append(f"{random.randint(50, 100)}%")
                else:
                    row.append(make_word(2, 2))
            elif (
                "giá" in headers[j].lower()
                or "tiền" in headers[j].lower()
                or "thành" in headers[j].lower()
            ):
                row.append(f"{random.randint(10, 9999):,}")
            elif "lượng" in headers[j].lower() or "số" in headers[j].lower():
                row.append(str(random.randint(1, 500)))
            elif "thời" in headers[j].lower() or "ngày" in headers[j].lower():
                m = random.randint(1, 12)
                d = random.randint(1, 28)
                row.append(f"{d:02d}/{m:02d}/2025")
            else:
                row.append(make_word(1, 2))
        rows.append(row)
    return {"headers": headers, "rows": rows}


def make_section(section_number: int) -> dict:
    """Trả về dict {'title': str, 'paragraphs': [str], 'table': dict|None}"""
    title = random.choice(SECTION_TITLES).format(n=section_number)
    paragraphs = [make_paragraph() for _ in range(random.randint(2, 4))]
    table = make_table() if random.random() < 0.3 else None
    return {"title": title, "paragraphs": paragraphs, "table": table}


# ─────────────────────────────────────────────
# Sinh toàn bộ nội dung (dạng cấu trúc)
# ─────────────────────────────────────────────

WORDS_PER_PAGE = 500


def generate_content(pages: int = 7) -> dict:
    """Trả về dict chứa metadata + danh sách sections."""
    target_words = pages * WORDS_PER_PAGE
    title = random.choice(DOCUMENT_TITLES)
    sections = []
    total_words = 0
    section_num = 1

    while total_words < target_words:
        sec = make_section(section_num)
        word_count = sum(len(p.split()) for p in sec["paragraphs"]) + len(
            sec["title"].split()
        )
        sections.append(sec)
        total_words += word_count
        section_num += 1

    return {
        "title": title,
        "pages": pages,
        "sections": sections,
        "total_words": total_words,
        "unique_words": len(_generated_words),
        "section_count": section_num - 1,
    }


def title_to_filename(title: str) -> str:
    """Chuyển tiêu đề thành tên file không dấu, viết thường, nối bằng gạch dưới."""
    s = title.lower()
    # Replace Vietnamese diacritics
    s = re.sub(r"[àáảãạăằắẳẵặâầấẩẫậ]", "a", s)
    s = re.sub(r"[èéẻẽẹêềếểễệ]", "e", s)
    s = re.sub(r"[ìíỉĩị]", "i", s)
    s = re.sub(r"[òóỏõọôồốổỗộơờớởỡợ]", "o", s)
    s = re.sub(r"[ùúủũụưừứửữự]", "u", s)
    s = re.sub(r"[ỳýỷỹỵ]", "y", s)
    s = re.sub(r"[đ]", "d", s)
    s = re.sub(r"[^a-z0-9]+", "_", s)
    s = re.sub(r"_+", "_", s)
    s = s.strip("_")
    # Thêm hậu tố random 4 ký tự để không trùng
    suffix = hashlib.md5(f"{title}_{random.random()}".encode()).hexdigest()[:4]
    return f"{s[:45]}_{suffix}"


def save_txt(content: dict, output_path: str):
    lines = []
    for sec in content["sections"]:
        lines.append(sec["title"])
        lines.append("=" * len(sec["title"]))
        lines.append("")
        for para in sec["paragraphs"]:
            lines.append(para)
            lines.append("")
        if sec.get("table"):
            tbl = sec["table"]
            col_widths = [len(h) for h in tbl["headers"]]
            for row in tbl["rows"]:
                for j, val in enumerate(row):
                    col_widths[j] = max(col_widths[j], len(val))
            sep = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"
            header_line = (
                "|"
                + "|".join(
                    " {h:<{w}} ".format(h=h, w=col_widths[j])
                    for j, h in enumerate(tbl["headers"])
                )
                + "|"
            )
            lines.append(sep)
            lines.append(header_line)
            lines.append(sep)
            for row in tbl["rows"]:
                row_line = (
                    "|"
                    + "|".join(
                        " {v:<{w}} ".format(v=v, w=col_widths[j])
                        for j, v in enumerate(row)
                    )
                    + "|"
                )
                lines.append(row_line)
            lines.append(sep)
            lines.append("")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def save_pdf(content: dict, output_path: str):
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import cm
        from reportlab.lib import colors
        from reportlab.platypus import (
            SimpleDocTemplate,
            Paragraph,
            Spacer,
            HRFlowable,
            Table,
            TableStyle,
        )
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        import platform
    except ImportError:
        print(
            "[ERROR] Chưa cài reportlab. Chạy: pip install reportlab", file=sys.stderr
        )
        sys.exit(1)

    font_name = "Helvetica"
    font_candidates = []

    system = platform.system()
    if system == "Linux":
        font_candidates = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
            "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
            "/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf",
        ]
    elif system == "Windows":
        font_candidates = [
            "C:/Windows/Fonts/arial.ttf",
            "C:/Windows/Fonts/times.ttf",
        ]
    elif system == "Darwin":
        font_candidates = [
            "/Library/Fonts/Arial.ttf",
            "/System/Library/Fonts/Supplemental/Arial.ttf",
        ]

    for path in font_candidates:
        if os.path.exists(path):
            try:
                pdfmetrics.registerFont(TTFont("CustomFont", path))
                font_name = "CustomFont"
                break
            except Exception:
                continue

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "DocTitle",
        fontName=font_name,
        fontSize=16,
        leading=22,
        textColor=colors.HexColor("#1a1a2e"),
        spaceAfter=6,
        alignment=1,
    )
    heading_style = ParagraphStyle(
        "SectionHeading",
        fontName=font_name,
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#2c3e8c"),
        spaceBefore=18,
        spaceAfter=6,
        fontWeight="bold",
    )
    body_style = ParagraphStyle(
        "Body",
        fontName=font_name,
        fontSize=10,
        leading=15,
        textColor=colors.HexColor("#222222"),
        spaceAfter=10,
        firstLineIndent=18,
        alignment=4,
    )

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=2.5 * cm,
        rightMargin=2.5 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2.5 * cm,
        title=content["title"],
        author="random_text_generator",
    )

    story = []

    story.append(Spacer(1, 0.5 * cm))
    story.append(Paragraph(content["title"], title_style))
    story.append(
        HRFlowable(
            width="100%", thickness=1.5, color=colors.HexColor("#2c3e8c"), spaceAfter=16
        )
    )

    for sec in content["sections"]:
        story.append(Paragraph(sec["title"], heading_style))
        story.append(
            HRFlowable(
                width="100%",
                thickness=0.5,
                color=colors.HexColor("#dddddd"),
                spaceAfter=6,
            )
        )
        for para in sec["paragraphs"]:
            safe_para = (
                para.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            )
            story.append(Paragraph(safe_para, body_style))
        if sec.get("table"):
            tbl = sec["table"]
            data = [tbl["headers"]] + tbl["rows"]
            col_widths = [(11 * cm) / len(tbl["headers"])] * len(tbl["headers"])
            table = Table(data, colWidths=col_widths)
            table.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2c3e8c")),
                        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                        ("FONTNAME", (0, 0), (-1, 0), font_name),
                        ("FONTSIZE", (0, 0), (-1, 0), 9),
                        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
                        ("FONTNAME", (0, 1), (-1, -1), font_name),
                        ("FONTSIZE", (0, 1), (-1, -1), 8),
                        (
                            "ROWBACKGROUNDS",
                            (0, 1),
                            (-1, -1),
                            [colors.white, colors.HexColor("#f5f5f5")],
                        ),
                        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ]
                )
            )
            story.append(Spacer(1, 0.3 * cm))
            story.append(table)
            story.append(Spacer(1, 0.3 * cm))

    doc.build(story)


def generate_one_file(pages: int, fmt: str, output_dir: str, output: str = None) -> str:
    """Sinh 1 file, trả về đường dẫn file đã lưu."""
    content = generate_content(pages=pages)
    if output is None:
        filename = title_to_filename(content["title"])
        output = f"{filename}.{fmt}"
    base, ext = os.path.splitext(output)
    if ext.lower() != f".{fmt}":
        output = f"{base}.{fmt}"

    output_path = os.path.join(output_dir, os.path.basename(output))
    if fmt == "pdf":
        save_pdf(content, output_path)
    else:
        save_txt(content, output_path)
    return output_path


def main():

    output_dir = OUTPUT_DIR if OUTPUT_DIR else os.getcwd()
    os.makedirs(output_dir, exist_ok=True)

    if FILE_COUNT == 1 and OUTPUT_NAME:
        pages = PAGES if PAGES else random.randint(5, 10)
        output = generate_one_file(
            pages,
            OUTPUT_FORMAT,
            output_dir,
            OUTPUT_NAME,
        )
        print(f"[OK] Đã lưu: {output}", file=sys.stderr)
    else:
        if OUTPUT_NAME and FILE_COUNT > 1:
            print("[WARN] OUTPUT_NAME bị bỏ qua khi tạo nhiều file.", file=sys.stderr)

        for i in range(FILE_COUNT):
            pages = PAGES if PAGES else random.randint(5, 10)
            output = generate_one_file(
                pages,
                OUTPUT_FORMAT,
                output_dir,
            )
            print(
                f"[OK] [{i+1}/{FILE_COUNT}] Đã lưu: {output} ({pages} trang)",
                file=sys.stderr,
            )


if __name__ == "__main__":
    main()
