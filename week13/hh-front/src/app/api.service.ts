import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from "rxjs";
import { Company } from "./company";
import { Vacancy } from "./vacancy";

@Injectable({
  providedIn: 'root'
})
export class APIService {

  constructor(private http: HttpClient ) { }
  getCompanies(): Observable<Company[]> {
    return this.http.get<Company[]>('http://localhost:8000/api/compamies/');
  }
  getVacanciesByCompanyId(companyId): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>('http://localhost:8000/api/companies/${companyId}/vacancies/');
  }
}
