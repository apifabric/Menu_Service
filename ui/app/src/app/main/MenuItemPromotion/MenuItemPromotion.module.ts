import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {MENUITEMPROMOTION_MODULE_DECLARATIONS, MenuItemPromotionRoutingModule} from  './MenuItemPromotion-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    MenuItemPromotionRoutingModule
  ],
  declarations: MENUITEMPROMOTION_MODULE_DECLARATIONS,
  exports: MENUITEMPROMOTION_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class MenuItemPromotionModule { }