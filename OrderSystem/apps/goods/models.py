from django.db import models
from utils.models import BaseModel


# Create your models here.


class GoodsCategory(BaseModel):
    """商品类别表"""
    name = models.CharField(max_length=20, verbose_name="名称")

    class Meta:
        db_table = "goods_category"
        verbose_name = "商品类别"  # admin站点使用
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# class Goods(BaseModel):
#     """商品SPU表"""
#     name = models.CharField(max_length=100, verbose_name="名称")
#
#     class Meta:
#         db_table = "goods"
#         verbose_name = "商品"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name


class GoodsSKU(BaseModel):
    """商品SKU表"""
    category = models.ForeignKey(GoodsCategory, verbose_name="类别")
    # goods = models.ForeignKey(Goods, verbose_name="商品")
    name = models.CharField(max_length=100, verbose_name="名称")
    unit = models.CharField(max_length=10, verbose_name="销售单位")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="价格")
    sales = models.IntegerField(default=0, verbose_name="销量")
    status = models.BooleanField(default=True, verbose_name="是否上线")

    class Meta:
        db_table = "goods_sku"
        verbose_name = "商品SKU"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(BaseModel):
    """商品图片"""
    sku = models.ForeignKey(GoodsSKU, verbose_name="商品SKU")
    image = models.ImageField(upload_to="goods", verbose_name="图片")

    class Meta:
        db_table = "goods_image"
        verbose_name = "商品图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.sku)

