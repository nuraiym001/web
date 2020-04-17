import { Component, OnInit } from '@angular/core';
import { Company } from "../company";
import { APIService } from "../api.service";

@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.css']
})
export class CompaniesComponent implements OnInit {

  companies: Company[];

  constructor(
    private apiService: APIService
  ) { }

  ngOnInit(): void {
  }
  getCompanies(): void {
    this.apiService.getCompanies().subscribe(companies=> this.companies = companies);
  }
}
