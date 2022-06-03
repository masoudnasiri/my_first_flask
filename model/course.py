
class Course:

    def __init__(self, category_title = "", subcategory_id = -1 , subcategory_title = "" , subcategori_discription = "" , subcategory_url = "" , course_id = -1 , course_title ="" ,course_url="" , num_of_subscribers=0 , avg_rating=0.0 , num_of_reviews=0):
        self.category_title=category_title
        self.subcategory_id= subcategory_id
        self.subcategory_id = subcategory_id
        self.subcategory_title = subcategory_title
        self.subcategori_discription = subcategori_discription
        self.subcategory_url = subcategory_url
        self.course_id = course_id
        self.course_title = course_title
        self.course_url = course_url
        self.num_of_subscribers=num_of_subscribers
        self.avg_rating = avg_rating
        self.num_of_reviews = num_of_reviews


    def __str__(self):
        return f"{self.category_title};;;{self.subcategory_id};;;{self.subcategory_title};;;{self.subcategory_url};;;{self.subcategori_discription};;;{self.course_id};;;{self.course_title};;;{self.course_url};;;{self.num_of_subscribers};;;{self.avg_rating};;;{self.num_of_reviews}"

    def get_courses(self):
        pass

    def clear_course_data(self):
        path = os.path.dirname(__file__)
        path = path.replace("model", "")
        user_data = open(path + "data\\course.txt", "w")
        user_data.close()


    def generate_page_num_list(self, page, total_pages):
        pass

    def get_courses_by_page(self, page):
        pass

    def delete_course_by_id(self, temp_course_id):
        pass

    def get_course_by_course_id(self, temp_course_id):
        pass

    def get_course_by_instructor_id(self, instructor_id):
        pass

    def generate_course_figure1(self):
        pass

    def generate_course_figure2(self):
        pass

    def generate_course_figure3(self):
        pass

    def generate_course_figure4(self):
        pass

    def generate_course_figure5(self):
        pass

    def generate_course_figure6(self):
        pass
