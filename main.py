import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain_ollama import ChatOllama
from inspect import signature


load_dotenv()
def main():
    print("Hello from langchain-course!")
    information = """
        Elon Reeve Musk ( / ˈ iː l ɒ n / EE -lon ; sinh ngày 28 tháng 6 năm 1971) là một doanh nhân và cựu quan chức nhà nước nổi tiếng với vai trò lãnh đạo Tesla và SpaceX . Musk đã là người giàu nhất thế giới kể từ năm 2025; tính đến tháng 6 năm 2026, Forbes ước tính giá trị tài sản ròng của ông là 834 tỷ đô la Mỹ.
Sinh ra trong một gia đình giàu có ở Pretoria , Nam Phi, Musk di cư đến Canada vào năm 1989; ông có quốc tịch Canada vì mẹ ông sinh ra ở đó. Ông nhận bằng cử nhân năm 1997 từ Đại học Pennsylvania trước khi chuyển đến California để theo đuổi các dự án kinh doanh. Năm 1995, Musk đồng sáng lập công ty phần mềm Zip2 . Sau khi bán công ty này vào năm 1999, ông đồng sáng lập X.com , một công ty thanh toán trực tuyến sau này sáp nhập để tạo thành PayPal , được eBay mua lại vào năm 2002. Musk cũng trở thành công dân Mỹ vào năm 2002.
Năm 2002, Musk thành lập công ty công nghệ vũ trụ SpaceX, trở thành Giám đốc điều hành kiêm kỹ sư trưởng ; kể từ đó, công ty đã dẫn đầu các đổi mới trong lĩnh vực tên lửa tái sử dụng và du hành vũ trụ thương mại . Musk gia nhập hãng sản xuất ô tô Tesla với tư cách là nhà đầu tư ban đầu vào năm 2004 và trở thành Giám đốc điều hành kiêm kiến ​​trúc sư sản phẩm vào năm 2008; kể từ đó, Tesla đã trở thành một trong những công ty hàng đầu về xe điện . Năm 2015, ông đồng sáng lập OpenAI để thúc đẩy nghiên cứu trí tuệ nhân tạo (AI), nhưng sau đó đã rời đi; Sự bất mãn ngày càng tăng với định hướng và khả năng lãnh đạo của tổ chức trong thời kỳ bùng nổ trí tuệ nhân tạo (AI) những năm 2020 đã dẫn ông đến việc thành lập xAI , sau đó trở thành công ty con của SpaceX vào năm 2026. Năm 2022, ông mua lại mạng xã hội Twitter, thực hiện những thay đổi đáng kể và đổi tên thành X vào năm 2023. Các doanh nghiệp khác của ông bao gồm công ty công nghệ thần kinh Neuralink , do ông đồng sáng lập năm 2016, và công ty đào hầm Boring Company , do ông thành lập năm 2017. Tháng 11 năm 2025, Tesla đã phê duyệt gói lương trị giá 1 nghìn tỷ đô la cho Musk, số tiền này sẽ được nhận trong vòng 10 năm nếu ông đạt được các mục tiêu cụ thể.
Musk là người ủng hộ các chính trị, nhân vật và đảng phái cực hữu toàn cầu. Ông là nhà tài trợ lớn nhất trong cuộc bầu cử tổng thống Mỹ năm 2024 , nơi ông ủng hộ Donald Trump . Sau khi Trump nhậm chức tổng thống vào tháng 1 năm 2025, Musk giữ chức Cố vấn cấp cao cho Tổng thống và là người đứng đầu trên thực tế của Bộ Hiệu quả Chính phủ (DOGE). Ngay trước khi xảy ra mâu thuẫn công khai với Trump , Musk rời chính quyền Trump vào tháng 5 năm 2025 và trở lại điều hành các công ty của mình.
    """

    # summary_template = """
    #     given a information {information} about a person I want you to create:
    #     1. A short summary
    #     2. two interesting facts about them
    # """

    summary_template = """
        Cho thông tin sau đây về một người: {information}
            Tôi muốn bạn tạo:
            1. Một bản tóm tắt ngắn gọn về người đó.
            2. Hai sự thật/thông tin thú vị về họ.
    """

    summary_promt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatAnthropic(model_name="claude-sonnet-4-6", temperature=0)
    #llm = ChatOllama(model="gemma4", temperature=0)

    chain = summary_promt_template | llm
    response = chain.invoke(input={"information":information})
    print(response.content)

    # print(signature(ChatAnthropic))
if __name__ == "__main__":
    main()
