import { Component, OnInit } from '@angular/core';
import { CompanyService } from '../company.service';
import { Company } from '../models';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.css']
})
export class CompanyComponent implements OnInit {
  companies: Company[] = [];

  constructor(public companyService: CompanyService,
              private route: ActivatedRoute) { }
 
  ngOnInit(): void {
    this.getCompanyList();
  }

  getCompanyList() {
    this.companyService.getCompanyList().subscribe(companies => {this.companies = companies; });
  }

}