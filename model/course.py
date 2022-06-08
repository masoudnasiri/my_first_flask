import os,codecs,json,itertools,pandas,matplotlib.pyplot as plt

from operator import attrgetter
class Course:

    def __init__(self, category_title = "", subcategory_id = -1 , subcategory_title = "" , subcategory_description = "" , subcategory_url = "" , course_id = -1 , course_title ="" ,course_url="" , num_of_subscribers=0 , avg_rating=0.0 , num_of_reviews=0):
        self.category_title=category_title
        self.subcategory_id= subcategory_id
        self.subcategory_id = subcategory_id
        self.subcategory_title = subcategory_title
        self.subcategory_description = subcategory_description
        self.subcategory_url = subcategory_url
        self.course_id = course_id
        self.course_title = course_title
        self.course_url = course_url
        self.num_of_subscribers=num_of_subscribers
        self.avg_rating = avg_rating
        self.num_of_reviews = num_of_reviews


    def __str__(self):
        return f"{self.category_title};;;{self.subcategory_id};;;{self.subcategory_title};;;{self.subcategory_url};;;" \
               f"{self.subcategory_description};;;{self.course_id};;;{self.course_title};;;{self.course_url};;;" \
               f"{self.num_of_subscribers};;;{self.avg_rating};;;{self.num_of_reviews}"

    def get_courses(self):
        path = os.path.dirname(__file__).replace("\\model", "") + "\\data\\source_course_files"
        course_file_path = os.path.dirname(__file__).replace("\\model", "") + "\\data\\course.txt"
        course_file = codecs.open(course_file_path, encoding="utf-8", mode="r+")

        evaluate = lambda x: x if (x != "") else "None"
        for root, dirs, files in os.walk(path):
            for file in files:
                with codecs.open(os.path.join(root, file),encoding="utf-8",mode="r") as coursedata:
                    all_data = json.load(coursedata)
                    #category_title=evaluate(all_data["unitinfo"]["category"])
                    raw_category=root.split("\\")[-2]
                    category_title=raw_category[10:].replace("_"," ")
                    subcategory_dic=evaluate(all_data["unitinfo"]["source_objects"][0])
                    subcategory_id=evaluate(subcategory_dic["id"])
                    subcategory_title=evaluate(subcategory_dic["title"])
                    subcategory_url=evaluate(subcategory_dic["url"])
                    subcategory_description=evaluate(subcategory_dic["description"])
                    for data in all_data["unitinfo"]["items"]:
                        course_id=evaluate(data["id"])
                        course_title=evaluate(data["title"])
                        course_url=evaluate(data["url"])
                        num_of_subscribers=evaluate(data["num_subscribers"])
                        avg_rating=evaluate(data["avg_rating"])
                        num_of_reviews=evaluate(data["num_reviews"])
                        course_file.write(f"{category_title};;;{subcategory_id};;;{subcategory_title};;;{subcategory_url};;;{subcategory_description};;;{course_id};;;{course_title};;;{course_url};;;{num_of_subscribers};;;{avg_rating};;;{num_of_reviews}\n")
                        test=f"{category_title};;;{subcategory_id};;;{subcategory_title};;;{subcategory_url};;;"\
                             f"{subcategory_description};;;{course_id};;;{course_title};;;{course_url};;;{num_of_subscribers};;;{avg_rating};;;{num_of_reviews}\n"
                        if len(test.split(";;;"))>11:
                            print(test.split(";;;"))
        course_file.close()

    def clear_course_data(self):
        course_file_path = os.path.dirname(__file__).replace("\\model", "") + "\\data\\course.txt"
        course_file = codecs.open(course_file_path, encoding="utf-8", mode="w")
        course_file.close()


    def generate_page_num_list(self, page, total_pages):
        if page<=5:
            viewbale_pages=list(range(1,10))
        elif page>5 and page<(total_pages-4):
            viewbale_pages=list(range(page-4,page+5))
        elif page>=(total_pages-4):
            viewbale_pages=list((total_pages-8,total_pages+1))
        return viewbale_pages

    def get_courses_by_page(self, page):
        path=os.path.dirname(__file__).replace("\\model", "") + "\\data\\course.txt"
        with codecs.open(path,encoding="utf-8",mode="r") as course_data:
            courses=course_data.readlines()
            course_list=[]
            pages_dic={}
            for course in courses:
                one_course=course.split(";;;")
                course_obj=Course(one_course[0],one_course[1],one_course[2],one_course[3],one_course[4],one_course[5],
                                  one_course[6],one_course[7],one_course[8],one_course[9],one_course[10])
                course_list.append(course_obj)
        if len(course_list)%20!=0:
            total_pages=(len(course_list)//20)+1
        else:
            total_pages=len(course_list)//20
        for i in range(total_pages):
            pages_dic[i]=course_list[i:i+20]
        return (pages_dic[page],total_pages,len(course_list))

    def delete_course_by_id(self, temp_course_id):
        id = str(temp_course_id)
        # list to store file lines
        lines = []
        # read file
        error=[]
        path = os.path.dirname(__file__).replace("\\model", "") + "\\data\\course.txt"
        with codecs.open(path, encoding="utf", mode="r") as fp:
            # read an store all lines into list
            data=fp.read()
            list=data.split("\n")
        with codecs.open(path, encoding="utf", mode="w") as fp:
            for item in list:
                temp_course=item.split(";;;")
                if len(item.split(";;;"))==11:
                    if item.split(";;;")[5]!=id:
                        fp.write(item)
                        fp.write("\n")
                else:
                    print(item)
    def get_course_by_course_id(self, temp_course_id):
        temp_course_id=str(temp_course_id)
        path = os.path.dirname(__file__).replace("\\model", "") + "\\data\\course.txt"
        found_flag=0
        with codecs.open(path, encoding="utf", mode="r") as fp:
            list=fp.readlines()
            for item in list:
                one_course=item.split(";;;")

                if len(one_course)==11:
                    if one_course[5]==temp_course_id:
                        course_obj=Course(one_course[0],one_course[1],one_course[2],one_course[3],one_course[4],one_course[5],
                                  one_course[6],one_course[7],one_course[8],one_course[9],one_course[10])
                        found_flag=1
        if found_flag==1:
            if int(course_obj.num_of_subscribers) > 100000 and float(course_obj.avg_rating) > 4.5 and int(
                    course_obj.num_of_reviews) > 10000:
                comment = "Top Course"
            elif int(course_obj.num_of_subscribers) > 50000 and int(course_obj.avg_rating) > 4 and int(
                    course_obj.num_of_reviews) > 5000:
                comment = "Popular Courses"
            elif int(course_obj.num_of_subscribers) > 10000 and float(course_obj.avg_rating) > 3.5 and int(
                    course_obj.num_of_reviews) > 1000:
                comment = "Good Courses”"
            else:
                comment = "General Course"
            return (course_obj,comment)
        else:
            return ("None","None")

    def get_course_by_instructor_id(self, instructor_id):
        instructor_id=str(instructor_id)
        path = os.path.dirname(__file__).replace("\\model", "") + "\\data\\user.txt"
        with codecs.open(path, encoding="utf-8", mode="r") as user_data:
            users = user_data.readlines()
            course_list = []
            for user in users:
                one_user = user.split(";;;")
                if one_user[0]==instructor_id and one_user[4] == "instructor":
                    one_user=one_user[-1].split("\n")
                    course_list=one_user[0].split("--")
        total_courses=len(course_list)
        if(total_courses>20):
            course_list=course_list[0:20]
        path = os.path.dirname(__file__).replace("\\model", "") + "\\data\\course.txt"
        course_obj_list=[]

        with codecs.open(path, encoding="utf", mode="r") as fp:
            lists = fp.readlines()
            for item in lists:
                one_course = item.split(";;;")

                if len(one_course) == 11:
                    if one_course[5] in course_list:
                        course_obj = Course(one_course[0], one_course[1], one_course[2], one_course[3], one_course[4],
                                            one_course[5],
                                            one_course[6], one_course[7], one_course[8], one_course[9], one_course[10])
                        course_obj_list.append(course_obj)
        return (course_obj_list,total_courses)

    def generate_course_figure1(self):
        path=os.path.dirname(__file__).replace("\\model", "") + "\\data\\course.txt"
        with codecs.open(path,encoding="utf-8",mode="r") as course_data:
            courses=course_data.readlines()
            course_obj_list=[]
            for course in courses:
                one_course=course.split(";;;")
                if len(one_course) == 11:
                    course_obj = Course(one_course[0], one_course[1], one_course[2], one_course[3], one_course[4],
                                        one_course[5],
                                        one_course[6], one_course[7], one_course[8], one_course[9], one_course[10])
                    course_obj_list.append(course_obj)
        course_dic_list={}
        sub_cat_seen=set()
        for item in course_obj_list:
            if item.subcategory_id not in sub_cat_seen:
                sub_cat_seen.add(item.subcategory_id)
                course_dic_list[item.subcategory_title]=int(item.num_of_subscribers)
            else:
                subscribers=course_dic_list[item.subcategory_title]
                course_dic_list[item.subcategory_title]=int(item.num_of_subscribers)+subscribers

        course_dic_list=dict(sorted(course_dic_list.items(), key=lambda item: item[1],reverse=True))
        course_dic_list=dict(itertools.islice(course_dic_list.items(), 10))

        sub_cat=list(course_dic_list.keys())

        for item in sub_cat:
            temp_sub=item.split()
            if len(temp_sub)>2:
                sub_cat[sub_cat.index(item)]=temp_sub[0]+" "+temp_sub[1]+" "+temp_sub[2]
        print(sub_cat)
        num_of_subscribers=list(course_dic_list.values())

        plt.bar(range(len(course_dic_list)), num_of_subscribers, tick_label=sub_cat)
        plt.show()
        return ("This Method Display a Graph for top 10 Subcategories")

    def generate_course_figure2(self):
        path = os.path.dirname(__file__).replace("\\model", "") + "\\data\\course.txt"
        with codecs.open(path, encoding="utf-8", mode="r") as course_data:
            courses = course_data.readlines()
            course_obj_list = []
            for course in courses:
                one_course = course.split(";;;")
                if len(one_course) == 11:
                    course_obj = Course(one_course[0], one_course[1], one_course[2], one_course[3], one_course[4],
                                        one_course[5],
                                        one_course[6], one_course[7], one_course[8], one_course[9], one_course[10])
                    course_obj_list.append(course_obj)
        course_dic_list = {}
        for item in course_obj_list:
            if int(item.num_of_reviews)>50000:
                title_list=item.course_title.split()
                if len(title_list)>2:
                    item.course_title = title_list[0]+" "+title_list[1]+" "+title_list[2]
                course_dic_list[item.course_title]=item.avg_rating
        course_dic_list = dict(sorted(course_dic_list.items(), key=lambda item: item[1]))

        course_dic_list=dict(itertools.islice(course_dic_list.items(), 10))
        sub_cat=list(course_dic_list.keys())
        num_of_subscribers=list(course_dic_list.values())

        plt.bar(range(len(course_dic_list)), num_of_subscribers, tick_label=sub_cat)
        plt.show()
        return("Generate a graph to show the top 10 courses that have lowest avg rating and over 50000 reviews")


    def generate_course_figure3(self):
        path = os.path.dirname(__file__).replace("\\model", "") + "\\data\\course.txt"
        with codecs.open(path, encoding="utf-8", mode="r") as course_data:
            courses = course_data.readlines()
            course_obj_list = []
            for course in courses:
                one_course = course.split(";;;")
                if len(one_course) == 11:
                    course_obj = Course(one_course[0], one_course[1], one_course[2], one_course[3], one_course[4],
                                        one_course[5],
                                        one_course[6], one_course[7], one_course[8], one_course[9], one_course[10])
                    course_obj_list.append(course_obj)
        course_dic_list = {}
        for item in course_obj_list:
            if int(item.num_of_subscribers)>10000 and int(item.num_of_subscribers)<100000:
                course_dic_list[int(item.num_of_subscribers)]=float(item.avg_rating)
        course_subscribers=list(course_dic_list.keys())
        average_rate=list(course_dic_list.values())
        plt.scatter(course_subscribers,average_rate)
        plt.show()
        return "Generate a graph to show the all the courses avg rating distribution that has subscribers between 100000 and 10000 "


    def generate_course_figure4(self):
        path = os.path.dirname(__file__).replace("\\model", "") + "\\data\\course.txt"
        with codecs.open(path, encoding="utf-8", mode="r") as course_data:
            courses = course_data.readlines()
            course_obj_list = []
            for course in courses:
                one_course = course.split(";;;")
                if len(one_course) == 11:
                    course_obj = Course(one_course[0], one_course[1], one_course[2], one_course[3], one_course[4],
                                        one_course[5],
                                        one_course[6], one_course[7], one_course[8], one_course[9], one_course[10])
                    course_obj_list.append(course_obj)
        course_dic_list = {}
        cat_seen = set()
        for item in course_obj_list:
            if item.category_title not in cat_seen:
                cat_seen.add(item.category_title)
                course_dic_list[item.category_title]= 1

            elif item.category_title in cat_seen:
                current_total=course_dic_list[item.category_title]
                course_dic_list[item.category_title]=current_total+1
        course_dic_list=dict(sorted(course_dic_list.items(), key=lambda item: item[1]))
        category=list(course_dic_list.keys())
        total_course=list(course_dic_list.values())
        explode=[]
        for item in total_course:
            explode.append(0)
        explode[-2]=0.2
        plt.pie(total_course, labels=category, explode=explode)
        plt.show()

    def generate_course_figure5(self):
        path = os.path.dirname(__file__).replace("\\model", "") + "\\data\\course.txt"
        with codecs.open(path, encoding="utf-8", mode="r") as course_data:
            courses = course_data.readlines()
            agenda=["reviewed Courses","Without Review Courses"]
            data= [0,0]
            for course in courses:
                one_course = course.split(";;;")
                if len(one_course) == 11:
                    if int(course.split(";;;")[10].strip('.\n')) > 0:
                        data[0]=data[0]+1
                    else:
                        data[1]=data[1]+1
            plt.bar(range(len(agenda)), data, tick_label=agenda)
            plt.show()

            return "This graph show How many courses did reviewed and how many didn't"

    def generate_course_figure6(self):
        path=os.path.dirname(__file__).replace("\\model", "") + "\\data\\course.txt"
        with codecs.open(path,encoding="utf-8",mode="r") as course_data:
            courses=course_data.readlines()
            course_obj_list=[]
            for course in courses:
                one_course=course.split(";;;")
                if len(one_course) == 11:
                    course_obj = Course(one_course[0], one_course[1], one_course[2], one_course[3], one_course[4],
                                        one_course[5],
                                        one_course[6], one_course[7], one_course[8], one_course[9], one_course[10])
                    course_obj_list.append(course_obj)
        course_dic_list={}
        sub_cat_seen=set()
        for item in course_obj_list:
            if item.subcategory_id not in sub_cat_seen:
                sub_cat_seen.add(item.subcategory_id)
                course_dic_list[item.subcategory_title]=1
            else:
                total_courses=course_dic_list[item.subcategory_title]
                course_dic_list[item.subcategory_title]=total_courses+1

        course_dic_list=dict(sorted(course_dic_list.items(), key=lambda item: item[1]))
        course_dic_list=dict(itertools.islice(course_dic_list.items(), 10))

        sub_cat=list(course_dic_list.keys())
        for item in sub_cat:
            temp_sub=item.split()
            if len(temp_sub)>2:
                sub_cat[sub_cat.index(item)]=temp_sub[0]+" "+temp_sub[1]+" "+temp_sub[2]

        number_of_courses=list(course_dic_list.values())

        plt.bar(range(len(course_dic_list)), number_of_courses, tick_label=sub_cat)
        plt.show()
        return ("This Method Display a Graph for top 10 Subcategories")

