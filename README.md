# Api-rest-django
This project is an api rest build for the treina web course "creating rest apis with django" 
                and its made with sqlite, python, django and django rest framework.
                The main purpose of the project is to add jobs in it and add technologies to a job like linkedin, glassdoor etc.


<p>TECHNOLOGIES</p>
 <table >
                    <thead>
                        <tr>
                            <th>Operations</th>
                            <th>Params</th>
                            <th>URL</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>List Technologies method: GET</td>
                            <td>-</td>
                            <td>http://127.0.0.1:8000/api/technologies/</td>
                        </tr>
                        <tr>
                            <td>Find Especific Technology method: GET</td>
                            <td>
                                technology id in url
                            </td>
                            <td>
                                http://127.0.0.1:8000/api/technologies/id
                            </td>
                        </tr>
                        <tr>
                            <td>Insert Technology method: POST</td>
                            <td>
                                {
                                    "name": "Python"
                                }
                            </td>
                            <td>
                                http://127.0.0.1:8000/api/technologies/
                            </td>
                        </tr>
                        <tr>
                            <td>Update Technology method: PUT</td>
                            <td>
                                {
                                    "name": "Python"
                                }
                                technology id in url
                            </td>
                            <td>
                                http://127.0.0.1:8000/api/technologies/id
                            </td>
                        </tr>
                        <tr>
                           <td>Delete Technology method: DELETE</td>
                           <td>technology id in url  </td>
                           <td>http://127.0.0.1:8000/api/technologies/id</td>
                        </tr>
   </tbody>
</table>
<p class="collection-item">JOBS</p>
                <table>
                    <thead>
                        <tr>
                            <th>Operations</th>
                            <th>Params</th>
                            <th>URL</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>List Jobs method: GET</td>
                            <td>  
                            </td>
                            <td>
                                http://127.0.0.1:8000/api/jobs/
                            </td>
                        </tr>
                        <tr>
                            <td>Find Especific Job method: GET</td>
                            <td>
                                Job id in url
                            </td>
                            <td>
                                http://127.0.0.1:8000/api/jobs/id
                            </td>
                        </tr>
                        <tr>
                            <td>Insert Job method: POST</td>
                            <td>
                                {
                                    "title":"erlang developer",
                                    "description": "develop and deploy complex back-ends following solid and oop principles",
                                    "salary":2500,
                                    "company_name":"fictional company",
                                    "amount_of_jobs":2,
                                    "contact":"kevin.kds80@gmail.com",
                                    "type_of_job":"remote",
                                    "technologies":[1,2]
                                }
                            </td>
                            <td>
                                http://127.0.0.1:8000/api/jobs/
                            </td>
                        </tr>
                        <tr>
                            <td>Update Job method: PUT</td>
                            <td>
                                {
                                    "title":"updated developer",
                                    "description": "develop and deploy complex back-ends following solid and oop principles",
                                    "salary":2500,
                                    "company_name":"fictional company",
                                    "amount_of_jobs":2,
                                    "contact":"kevin.kds80@gmail.com",
                                    "type_of_job":"remote",
                                    "technologies":[1,2]
                                }
                                Job id in url
                            </td>
                            <td>
                                http://127.0.0.1:8000/api/jobs/id
                            </td>
                        </tr>
                        <tr>
                            <td>Delete Job method: DELETE</td>
                            <td>
                                Job id in url
                            </td>
                            <td>
                                http://127.0.0.1:8000/api/jobs/id
                            </td>
                        </tr>
                    </tbody>
                </table>
