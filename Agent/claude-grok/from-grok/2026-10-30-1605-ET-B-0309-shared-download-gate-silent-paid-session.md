Sent: 2026-10-30 16:05 ET

# B-0309 Shared download gate: Download does nothing, silently, for signed-in paid/admin sessions
Priority: P1 · Estimated effort: M · Report: QA-REPORT-160 addendum · Source: admin session ~16:00-16:02 ET (reproduced 15:47 and 16:01 ET); live JS read 16:04-16:05 ET (ToolPage-BILZoqti.js, YtThumbnail-HTZVbY8G.js)

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A paying customer who presses Download always gets the file, or a clear message saying why not.

## Why
Admin session, yt-thumbnail, reproduced twice (15:47 and 16:01 ET): Max-res and Standard Download → no network request, no usage.log, no download, no toast, no console error. Logged out, the same click saves youtube-<id>-maxresdefault.jpg (1280×720, checked 15:48 ET).
Live JS, as read: the shared download helper (exported from ToolPage as `d`, used by the shared Download button exported as `D`) wraps saving in `gate().then(ok => ok && save())`. If the gate resolves false or never resolves, nothing happens and nothing is shown; only a rejected gate shows "Couldn't check today's uses". The yt-thumbnail handler first awaits `logUsageNow()` and returns silently if it is false. With no request at all, the stop happens before the fetch: logUsageNow() returns false or hangs for this session. The gate's own error toast never appeared.
Paying users are the ones this hits, which makes it a revenue and refund risk.

Tools whose live chunks import the shared helper or the shared Download button (checked in the live JS 16:05 ET): AccessibilityCheckerPowerPoint, AcxChecker, AddPageNumbers, AgendaBuilder, ArrivalsDeparturesBoard, AudioCompressor, AudioConverter, AudioMerger, AudioNormalizer, AudioScrambler, AudioSpeedChanger, AudioToSubtitles, AudioTrimmer, AvatarBuilder, BankStatementToCsv, BannerSignMaker, BarcodeGenerator, Base64Tool, BatesNumbering, BlindCvRedactor, BookInteriorMaker, BookMaker, BookSpineCalculator, BoothLayoutPlanner, BrandKit, BrochureFlyerMaker, BulkImage, BulkQr, BusinessCard, CalendarInviteMaker, CameraCapture, CaseConverter, CatalogMaker, CateringQuantityCalculator, CertificateMaker, CleanPowerPoint, CollageMaker, ComparePdf, CompressImage, CompressPdf, CompressPowerPoint, CompressVideo, ConvertVideo, CopyrightPageMaker, CropPdf, CssJsMinifier, CsvConverter, CustomQr, DietaryAccessSummary, DigitalDownloadPackager, DocumentAssembler, DocumentScanner, EmailExtractor, EmailSignatureGenerator, EpubChecker, EpubMaker, EventBudgetPlanner, EventChecklistPlanner, EventClosureReportMaker, EventDaySchedule, EventLandingPageGenerator, EventProfitLedger, EventTaxSummary, ExcelToPdf, ExhibitStamper, ExhibitorBoothTracker, ExifRemover, ExpenseTracker, ExtractAudio, ExtractChartsPowerPoint, ExtractFromPowerPoint, ExtractPdf, FaviconGenerator, FillableForms, FindReplace, FindReplacePowerPoint, FlattenPdf, FlipRotateImage, GiveawayWinnerPicker, GroceryListPlanner, GuestListTracker, HtmlToPdf, ImageFilters, ImageSplitter, ImageToPdf, ImageToSvg, ImagesToPowerPoint, InvitationCardMaker, InvoiceGenerator, JsonCsvConverter, JsonFormatter, LabelSheetMaker, LegalProductionDesk, LogoMaker, LowContentInteriorMaker, MagazineMaker, MailMergePdf, ManuscriptFormatter, MarkdownEditor, MarkdownHtmlConverter, MarkdownToPowerPoint, MemeGenerator, MenuCardMaker, MerchandiseOrderSheet, MergePdf, MergePowerPoint, MergeVideo, Mesh3DConverter, MockupGenerator, MonthlyBudgetPlanner, MovingCostEstimator, NameBadgeMaker, NoiseRemover, OcrPdf, OcrTool, OgPreview, OnixGenerator, OpenHouseSignIn, OrganizePdf, OrganizeSlides, PaperSubmissionDesk, PassportPhoto, PasswordProtectPowerPoint, PdfBookmarksEditor, PdfEditor, PdfPassword, PdfToExcel, PdfToJpg, PdfToPowerPoint, PdfToWord, PdfWatermark, PeriodCalculator, PhotoSlideshowMaker, PowerPointTemplates, PowerPointToHtml, PowerPointToImages, PowerPointToPdf, PregnancyScanCalculator, PresentationStudio, QrGenerator, QrScanner, RandomNumberGenerator, ReceiptMaker, ReceiptToExpenseSheet, RedactPdf, RedactPowerPoint, RelocationChecklistPlanner, RemovePdfPages, RepairPdf, RepairPowerPoint, ReplaceFontsPowerPoint, ResizeCrop, ResizeSlides, ResumeBuilder, RingtoneMaker, RobotsSitemap, RoomingListPlanner, RotatePdf, RunOfShowCueSheet, ScreenRecorder, ScreenshotTool, SeatingChartPlanner, SellerPricingDesk, SellerStudio, SignPdf, SilenceRemover, SiteLaunchKit, SlideDeckMaker, SlideNumbersPowerPoint, SocialMediaFormatter, SplitPdf, SplitPowerPoint, SpriteSheetTool, SqlFormatter, StlAsciiBinaryConverter, StudentLoanCalculator, SubtitleAdder, TemplateThemeMaker, ThumbnailGen, TimesheetGenerator, TimezoneConverter, TravelItineraryPlanner, TrimVideo, UniversalFileConverter, UnlockPdf, UrlExtractor, VendorQuoteComparison, VideoToGif, VisitorLeadCaptureSheet, VoiceRecorder, VolumeBooster, WatermarkPowerPoint, WebpConverter, WordToPdf, YtThumbnail, ZipUnzip.
Not every one of these is proven broken. Only yt-thumbnail is reproduced. The others share the same code path.

## Who uses this
Every signed-in paying customer (day pass, monthly) and admins.

## Outcomes (ranked)
1. In a paid/admin session, every Download click either saves the file or shows a message saying why not. No silent return remains in logUsageNow, the gate or the helper.
2. If the usage check hangs, time out after a few seconds and either save (paid) or show "Couldn't check today's uses".
3. A paid session never waits on the trial counter to save a file.

## SEO
- Now: not an SEO item; no search impact expected.
- Keywords: n/a
- Suggested Title: keep
- Suggested Meta: keep
- Suggested H1: keep
- FAQ: keep

## Constraints
Logged-out trial counting stays as is: results and downloads count against the trial. Do not raise trial limits. Do not change download gating at 0 trial uses.

## Test cases
1. Admin/paid session, /tool/yt-thumbnail, dQw4w9WgXcQ → Get Thumbnails → Max-res Download → youtube-dQw4w9WgXcQ-maxresdefault.jpg (1280×720) saves.
2. Same with Standard → sddefault saves.
3. Paid session sweep: one download each on business-card, bulk-image, compress-pdf, merge-pdf, audio-trimmer, audio-merger, invoice-generator, qr-generator → a file each time.
4. Logged out with trial uses left → yt-thumbnail download still works and the counter drops by one.
5. Usage endpoint blocked in DevTools (paid session) → a message within a few seconds, never silence.
