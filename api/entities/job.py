class Job():
    def __init__(self, title, description, salary, company_name, amount_of_jobs, contact, type_of_job, technologies):
        self.__title = title
        self.__description = description
        self.__salary = salary
        self.__company_name = company_name
        self.__amount_of_jobs = amount_of_jobs
        self.__contact = contact
        self.__type_of_job = type_of_job
        self.__technologies = technologies


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    @property
    def company_name(self):
        return self.__company_name

    @company_name.setter
    def company_name(self, company_name):
        self.__company_name = company_name

    @property
    def amount_of_jobs(self):
        return self.__amount_of_jobs

    @amount_of_jobs.setter
    def amount_of_jobs(self, amount_of_jobs):
        self.__amount_of_jobs = amount_of_jobs

    @property
    def contact(self):
        return self.__contact

    @contact.setter
    def contact(self, contact):
        self.__contact = contact

    @property
    def type_of_job(self):
        return self.__type_of_job

    @type_of_job.setter
    def type_of_job(self, type_of_job):
        self.__type_of_job = type_of_job

    @property
    def technologies(self):
        return self.__technologies

    @technologies.setter
    def technologies(self, technologies):
        self.__technologies = technologies