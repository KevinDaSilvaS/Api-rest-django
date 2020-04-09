<table class="">
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
                            <td>
                                technology id in url
                            </td>
                            <td>
                                http://127.0.0.1:8000/api/technologies/id
                            </td>
                        </tr>
                    </tbody>
                </table>
